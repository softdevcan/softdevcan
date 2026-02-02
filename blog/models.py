from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

class AbstractModel(models.Model):
    """Base model for timestamped models"""
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated Date')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created Date')

    class Meta:
        abstract = True
        app_label = 'blog'


class Category(models.Model):
    """Blog post categories"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL Slug')
    description = models.TextField(blank=True, verbose_name='Description')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Blog post tags"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag Name')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL Slug')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(AbstractModel):
    """Blog post model with SEO and modern features"""
    # Basic fields
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL Slug',
                           help_text='Auto-generated from title if left blank')
    excerpt = models.TextField(max_length=500, blank=True, verbose_name='Excerpt',
                               help_text='Short summary for listing pages and meta description')
    content = models.TextField(verbose_name='Content')

    # Media
    image = models.ImageField(
        upload_to="blog_img/",
        blank=True,
        verbose_name='Featured Image',
        help_text='Main image for the post'
    )

    # Categorization
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Category'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Tags')

    # Metadata
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')

    CONTENT_TYPE_CHOICES = (
        ('article', 'Article'),
        ('poem', 'Poem'),
        ('tutorial', 'Tutorial'),
        ('news', 'News'),
        ('other', 'Other'),
    )
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='article')

    # Publishing
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Status')
    published_date = models.DateTimeField(null=True, blank=True, verbose_name='Published Date')

    # SEO fields
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta Description',
                                       help_text='SEO meta description (max 160 characters)')
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name='Meta Keywords',
                                    help_text='Comma-separated keywords for SEO')

    # Analytics
    view_count = models.PositiveIntegerField(default=0, verbose_name='View Count')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date', '-created_date']
        indexes = [
            models.Index(fields=['-published_date']),
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1

        # Auto-generate excerpt from content if not provided
        if not self.excerpt and self.content:
            self.excerpt = self.content[:200] + '...' if len(self.content) > 200 else self.content

        # Auto-generate meta_description from excerpt if not provided
        if not self.meta_description and self.excerpt:
            self.meta_description = self.excerpt[:160]

        # Set published_date when status changes to published
        if self.status == 'published' and not self.published_date:
            self.published_date = timezone.now()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def reading_time(self):
        """Estimate reading time in minutes"""
        word_count = len(self.content.split())
        minutes = max(1, word_count // 200)  # Average reading speed: 200 words/min
        return minutes
