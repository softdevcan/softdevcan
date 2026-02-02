from django.db import models
from django.urls import reverse

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated Date')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created Date')


    class Meta:
        abstract = True
        app_label = 'blog'  # Uygulama adını buraya ekleyin

class Post(AbstractModel):
    title = models.CharField(max_length=200)
    content = models.TextField(default='', blank=True, verbose_name='Content', help_text='')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to="blog_img/",
    )
    CONTENT_TYPE_CHOICES = (
        ('article', 'Makale'),
        ('poem', 'Şiir'),
        ('other', 'Diğer'),
    )
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='article')

    def __str__(self):
        return f'Post: {self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
