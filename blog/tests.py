import io
import os

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Category, Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpass123!')

    def test_auto_slug_generation(self):
        post = Post.objects.create(
            title='My First Blog Post',
            content='Some content here',
            author=self.user,
            status='published',
        )
        self.assertEqual(post.slug, 'my-first-blog-post')

    def test_auto_excerpt_generation(self):
        long_content = 'A' * 300
        post = Post.objects.create(
            title='Long Post',
            content=long_content,
            author=self.user,
        )
        self.assertTrue(len(post.excerpt) <= 204)  # 200 + '...'

    def test_published_date_set_on_publish(self):
        post = Post.objects.create(
            title='Draft Post',
            content='Content',
            author=self.user,
            status='draft',
        )
        self.assertIsNone(post.published_date)

        post.status = 'published'
        post.save()
        self.assertIsNotNone(post.published_date)

    def test_reading_time_property(self):
        # 400 words = 2 minutes at 200 words/min
        content = ' '.join(['word'] * 400)
        post = Post.objects.create(
            title='Reading Time Test',
            content=content,
            author=self.user,
        )
        self.assertEqual(post.reading_time, 2)

    def test_reading_time_minimum_one_minute(self):
        post = Post.objects.create(
            title='Short Post',
            content='Short',
            author=self.user,
        )
        self.assertEqual(post.reading_time, 1)


class PostMdFileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('mduser', 'md@test.com', 'testpass123!')

    def _make_md_file(self, content, name='post.md'):
        return SimpleUploadedFile(name, content.encode('utf-8'), content_type='text/markdown')

    def test_md_file_populates_content(self):
        md = self._make_md_file('# Hello\n\nThis is content.')
        post = Post.objects.create(
            title='MD Post', content='', author=self.user, md_file=md
        )
        self.assertEqual(post.content, '# Hello\n\nThis is content.')

    def test_no_md_file_keeps_manual_content(self):
        post = Post.objects.create(
            title='Manual Post', content='Manual content', author=self.user
        )
        self.assertEqual(post.content, 'Manual content')

    def test_updating_md_file_updates_content(self):
        md1 = self._make_md_file('# Version 1', name='v1.md')
        post = Post.objects.create(
            title='Versioned Post', content='', author=self.user, md_file=md1
        )
        self.assertEqual(post.content, '# Version 1')

        md2 = self._make_md_file('# Version 2', name='v2.md')
        post.md_file = md2
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.content, '# Version 2')

    def test_old_md_file_deleted_on_update(self):
        md1 = self._make_md_file('# V1', name='old.md')
        post = Post.objects.create(
            title='File Delete Test', content='', author=self.user, md_file=md1
        )
        old_path = post.md_file.path

        md2 = self._make_md_file('# V2', name='new.md')
        post.md_file = md2
        post.save()

        self.assertFalse(os.path.exists(old_path))

    def test_md_file_deleted_on_post_delete(self):
        md = self._make_md_file('# Delete me', name='todelete.md')
        post = Post.objects.create(
            title='Delete Post', content='', author=self.user, md_file=md
        )
        file_path = post.md_file.path
        post.delete()
        self.assertFalse(os.path.exists(file_path))


class CategoryModelTest(TestCase):
    def test_auto_slug_generation(self):
        category = Category.objects.create(name='Web Development')
        self.assertEqual(category.slug, 'web-development')


class BlogHomeViewTest(TestCase):
    def setUp(self):
        cache.clear()
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpass123!')

    def test_blog_home_loads(self):
        response = self.client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_only_published_posts_shown(self):
        Post.objects.create(
            title='Published Post', content='Content',
            author=self.user, status='published',
        )
        Post.objects.create(
            title='Draft Post', content='Content',
            author=self.user, status='draft',
        )
        response = self.client.get(reverse('blog_home'))
        self.assertContains(response, 'Published Post')
        self.assertNotContains(response, 'Draft Post')

    def test_search_functionality(self):
        Post.objects.create(
            title='Django Tutorial', content='Learn Django',
            author=self.user, status='published',
        )
        Post.objects.create(
            title='React Guide', content='Learn React',
            author=self.user, status='published',
        )
        response = self.client.get(reverse('blog_home') + '?q=Django')
        self.assertContains(response, 'Django Tutorial')
        self.assertNotContains(response, 'React Guide')


class BlogDetailViewTest(TestCase):
    def setUp(self):
        cache.clear()
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpass123!')
        self.post = Post.objects.create(
            title='Test Post', content='Content',
            author=self.user, status='published',
        )

    def test_blog_detail_loads(self):
        response = self.client.get(
            reverse('blog_detail', kwargs={'slug': self.post.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_count_increments(self):
        self.assertEqual(self.post.view_count, 0)
        self.client.get(
            reverse('blog_detail', kwargs={'slug': self.post.slug})
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.view_count, 1)

    def test_draft_post_returns_404(self):
        draft = Post.objects.create(
            title='Draft', content='Content',
            author=self.user, status='draft',
        )
        response = self.client.get(
            reverse('blog_detail', kwargs={'slug': draft.slug})
        )
        self.assertEqual(response.status_code, 404)


class RSSFeedTest(TestCase):
    def test_feed_returns_xml(self):
        response = self.client.get(reverse('blog_feed'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('xml', response['Content-Type'])
