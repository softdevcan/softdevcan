from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    """Modern category admin with Unfold"""
    list_display = ('name', 'slug', 'post_count', 'created_date')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

    @display(description=_("Posts"), ordering="post_count")
    def post_count(self, obj):
        """Display number of posts in category"""
        count = obj.posts.count()
        return format_html('<span style="color: #059669;">{} posts</span>', count)


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    """Modern tag admin with Unfold"""
    list_display = ('name', 'slug', 'post_count', 'created_date')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

    @display(description=_("Posts"), ordering="post_count")
    def post_count(self, obj):
        """Display number of posts with tag"""
        count = obj.posts.count()
        return format_html('<span style="color: #059669;">{} posts</span>', count)


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """Modern blog post admin with Unfold"""

    # List view configuration
    list_display = (
        'title',
        'status_badge',
        'author',
        'category',
        'content_type_badge',
        'view_count_display',
        'published_date'
    )
    list_display_links = ('title',)
    list_filter = (
        'status',
        'content_type',
        'category',
        'tags',
        'author',
        ('published_date', admin.DateFieldListFilter),
        ('created_date', admin.DateFieldListFilter),
    )
    search_fields = ('title', 'content', 'excerpt', 'meta_keywords', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created_date')
    filter_horizontal = ('tags',)
    readonly_fields = ('view_count', 'created_date', 'updated_date', 'word_count_display')
    list_per_page = 20

    # Actions
    actions = ['make_published', 'make_draft']

    # Fieldsets for better organization
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author')
        }),
        (_('Content'), {
            'fields': ('content_type', 'excerpt', 'content', 'image'),
            'description': 'Write your blog post content here. Markdown is supported.'
        }),
        (_('Categorization'), {
            'fields': ('category', 'tags'),
            'description': 'Organize your post with categories and tags'
        }),
        (_('Publishing'), {
            'fields': ('status', 'published_date'),
            'description': 'Control when and how your post is published'
        }),
        (_('SEO & Metadata'), {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',),
            'description': 'Improve search engine visibility'
        }),
        (_('Statistics'), {
            'fields': ('view_count', 'word_count_display', 'created_date', 'updated_date'),
            'classes': ('collapse',),
        }),
    )

    # Custom displays
    @display(description=_("Status"), ordering="status")
    def status_badge(self, obj):
        """Display status as colored badge"""
        colors = {
            'draft': '#6B7280',      # Gray
            'published': '#059669',  # Green
            'archived': '#DC2626',   # Red
        }
        color = colors.get(obj.status, '#6B7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px; font-weight: 600;">{}</span>',
            color,
            obj.get_status_display().upper()
        )

    @display(description=_("Type"), ordering="content_type")
    def content_type_badge(self, obj):
        """Display content type as badge"""
        icons = {
            'markdown': '📝 Markdown',
            'html': '🌐 HTML',
        }
        return format_html(
            '<span style="color: #059669; font-weight: 500;">{}</span>',
            icons.get(obj.content_type, obj.content_type)
        )

    @display(description=_("Views"), ordering="view_count")
    def view_count_display(self, obj):
        """Display view count with icon"""
        return format_html(
            '<span style="color: #6366F1;">👁️ {}</span>',
            obj.view_count
        )

    @display(description=_("Word Count"))
    def word_count_display(self, obj):
        """Calculate and display word count"""
        word_count = len(obj.content.split())
        return format_html(
            '<span style="color: #059669;">{} words</span>',
            word_count
        )

    # Actions
    @admin.action(description=_("Mark selected posts as Published"))
    def make_published(self, request, queryset):
        """Bulk action to publish posts"""
        from django.utils import timezone
        updated = queryset.update(status='published', published_date=timezone.now())
        self.message_user(request, f'{updated} posts marked as published.')

    @admin.action(description=_("Mark selected posts as Draft"))
    def make_draft(self, request, queryset):
        """Bulk action to draft posts"""
        updated = queryset.update(status='draft')
        self.message_user(request, f'{updated} posts marked as draft.')

    def save_model(self, request, obj, form, change):
        """Set author to current user if creating new post"""
        if not change:  # Only set author on creation
            obj.author = request.user

        # Auto-set published_date when status changes to published
        if obj.status == 'published' and not obj.published_date:
            from django.utils import timezone
            obj.published_date = timezone.now()

        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        qs = super().get_queryset(request)
        return qs.select_related('author', 'category').prefetch_related('tags')
