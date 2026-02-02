# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # SEO-friendly slug URL
]
