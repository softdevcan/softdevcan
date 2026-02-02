# blog/views.py

from django.shortcuts import render, get_object_or_404
from django.db.models import F, Q
from .models import Post

def blog_home(request):
    """Display published blog posts with search functionality"""
    posts = Post.objects.filter(status='published').select_related('author', 'category')

    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query) |
            Q(meta_keywords__icontains=search_query)
        )

    posts = posts[:10]

    context = {
        'posts': posts,
        'search_query': search_query,
    }
    return render(request, 'blog_home.html', context)


def blog_detail(request, slug):
    """Display single blog post and increment view count"""
    post = get_object_or_404(Post, slug=slug, status='published')

    # Increment view count atomically
    Post.objects.filter(pk=post.pk).update(view_count=F('view_count') + 1)
    post.refresh_from_db()

    context = {
        'post': post,
    }
    return render(request, 'blog_detail.html', context)


