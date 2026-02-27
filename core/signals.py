from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import (
    Document,
    Education,
    Experience,
    GeneralSetting,
    ImageSetting,
    Project,
    ProjectCategory,
    Skill,
    SocialMedia,
)


@receiver([post_save, post_delete], sender=GeneralSetting)
@receiver([post_save, post_delete], sender=ImageSetting)
@receiver([post_save, post_delete], sender=Document)
@receiver([post_save, post_delete], sender=SocialMedia)
def invalidate_layout_cache(sender, **kwargs):
    """Clear all cache when global settings change (affects all pages)"""
    cache.clear()


@receiver([post_save, post_delete], sender=Skill)
@receiver([post_save, post_delete], sender=Experience)
@receiver([post_save, post_delete], sender=Education)
def invalidate_home_cache(sender, **kwargs):
    """Clear entire cache when home page content changes"""
    cache.clear()


@receiver([post_save, post_delete], sender=Project)
@receiver([post_save, post_delete], sender=ProjectCategory)
def invalidate_portfolio_cache(sender, **kwargs):
    """Clear entire cache when portfolio content changes"""
    cache.clear()
