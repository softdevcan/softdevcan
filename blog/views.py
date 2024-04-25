# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('-created_date')[:5]  # En son 5 gönderiyi göster
    context = {
        'posts': posts,
    }
    return render(request, 'blog_home.html', context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog_detail.html', context)


