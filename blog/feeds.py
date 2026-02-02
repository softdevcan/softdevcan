# blog/feeds.py

from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    """RSS Feed for latest blog posts"""
    title = "Can Akyıldırım Blog"
    link = "/blog/"
    description = "Latest blog posts from Can Akyıldırım's software development blog."

    def items(self):
        return Post.objects.filter(status='published').order_by('-published_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt or item.content[:300]

    def item_link(self, item):
        return reverse('blog_detail', args=[item.slug])

    def item_pubdate(self, item):
        return item.published_date

    def item_author_name(self, item):
        if item.author:
            return item.author.get_full_name() or item.author.username
        return "Can Akyıldırım"

    def item_categories(self, item):
        categories = []
        if item.category:
            categories.append(item.category.name)
        categories.extend([tag.name for tag in item.tags.all()])
        return categories
