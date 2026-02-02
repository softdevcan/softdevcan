"""Markdown template tags for blog posts"""

import markdown as md
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """
    Convert markdown text to HTML with code highlighting support

    Usage in templates:
    {{ post.content|markdown }}
    """
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
    ]

    extension_configs = {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
        }
    }

    return mark_safe(md.markdown(value, extensions=extensions, extension_configs=extension_configs))
