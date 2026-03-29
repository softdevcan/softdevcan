import logging

from django.core.cache import cache
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver

from .models import Category, Post, Tag

logger = logging.getLogger(__name__)


@receiver([post_save, post_delete], sender=Post)
@receiver([post_save, post_delete], sender=Category)
@receiver([post_save, post_delete], sender=Tag)
def invalidate_blog_cache(sender, **kwargs):
    """Clear entire cache when blog content changes"""
    cache.clear()


@receiver(pre_delete, sender=Post)
def delete_post_md_file(sender, instance, **kwargs):
    """Delete md file from disk when post is deleted"""
    if instance.md_file and instance.md_file.name:
        try:
            instance.md_file.delete(save=False)
        except Exception:
            logger.exception("Failed to delete md_file for post pk=%s", instance.pk)
