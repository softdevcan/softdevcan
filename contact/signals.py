from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Message


@receiver([post_save, post_delete], sender=Message)
def invalidate_contact_cache(sender, **kwargs):
    """Clear cache when contact messages change (if needed for admin stats)"""
    # Contact messages don't affect frontend, but clear cache just in case
    cache.delete('layout_context')
