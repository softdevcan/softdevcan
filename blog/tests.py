from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from blog.models import Post, Category, Tag


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


class CategoryModelTest(TestCase):
    def test_auto_slug_generation(self):
        category = Category.objects.create(name='Web Development')
        self.assertEqual(category.slug, 'web-development')


class BlogHomeViewTest(TestCase):
    def setUp(self):
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
