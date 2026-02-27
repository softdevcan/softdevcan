from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Category, Post, Tag


@receiver([post_save, post_delete], sender=Post)
@receiver([post_save, post_delete], sender=Category)
@receiver([post_save, post_delete], sender=Tag)
def invalidate_blog_cache(sender, **kwargs):
    """Clear entire cache when blog content changes"""
    cache.clear()
