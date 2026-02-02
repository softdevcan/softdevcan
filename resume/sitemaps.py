# resume/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
from core.models import Project


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['index', 'portfolio', 'blog_home', 'contact']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    """Sitemap for blog posts"""
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Post.objects.filter(status='published').order_by('-published_date')

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])


class ProjectSitemap(Sitemap):
    """Sitemap for portfolio projects"""
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Project.objects.filter(is_published=True).order_by('-created_date')

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return reverse('project_detail', args=[obj.slug])
