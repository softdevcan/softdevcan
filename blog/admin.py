from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_date')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_date')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'status', 'published_date', 'view_count', 'content_type')
    list_filter = ('status', 'content_type', 'category', 'tags', 'author', 'created_date')
    search_fields = ('title', 'content', 'excerpt', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created_date')
    filter_horizontal = ('tags',)
    readonly_fields = ('view_count', 'created_date', 'updated_date')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'content_type', 'status')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'image')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('published_date',)
        }),
        ('Statistics', {
            'fields': ('view_count', 'created_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        """Set author to current user if creating new post"""
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
