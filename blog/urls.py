# blog/urls.py

from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('feed/', LatestPostsFeed(), name='blog_feed'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # SEO-friendly slug URL
]
