# Generated migration for blog model improvements

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        # Create Category model
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        # Create Tag model
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tag Name')),
                ('slug', models.SlugField(max_length=50, unique=True, verbose_name='URL Slug')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
            },
        ),
        # Add new fields to Post
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=250, unique=True, verbose_name='URL Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500, verbose_name='Excerpt'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='View Count'),
        ),
        # Add ForeignKey to Category
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.category', verbose_name='Category'),
        ),
        # Add ManyToMany to Tags
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.tag', verbose_name='Tags'),
        ),
        # Update existing fields
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_img/', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(choices=[('article', 'Article'), ('poem', 'Poem'), ('tutorial', 'Tutorial'), ('news', 'News'), ('other', 'Other')], default='article', max_length=20),
        ),
        # Add indexes
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-published_date'], name='blog_post_publish_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['slug'], name='blog_post_slug_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['status'], name='blog_post_status_idx'),
        ),
        # Update Meta
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date', '-created_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
