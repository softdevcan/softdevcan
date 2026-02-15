# blog/views.py

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Q
from .models import Post, Category

def blog_home(request):
    """Display published blog posts with search and category filter"""
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

    # Category filter
    category_slug = request.GET.get('category', '')
    active_category = None
    if category_slug:
        active_category = Category.objects.filter(slug=category_slug).first()
        if active_category:
            posts = posts.filter(category=active_category)

    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'blog_home.html', context)


def blog_detail(request, slug):
    """Display single blog post and increment view count"""
    post = get_object_or_404(
        Post.objects.select_related('author', 'category'),
        slug=slug,
        status='published',
    )

    # Increment view count atomically
    Post.objects.filter(pk=post.pk).update(view_count=F('view_count') + 1)
    post.refresh_from_db()

    # Previous and next posts for navigation
    previous_post = Post.objects.filter(
        status='published', published_date__lt=post.published_date
    ).order_by('-published_date').only('title', 'slug').first()

    next_post = Post.objects.filter(
        status='published', published_date__gt=post.published_date
    ).order_by('published_date').only('title', 'slug').first()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'blog_detail.html', context)


