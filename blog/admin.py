from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','image', 'created_date', 'updated_date', 'content_type')
    list_filter = ('author', 'created_date', 'updated_date', 'content_type')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    list_editable = ['image']

    class Meta:
        model = Post