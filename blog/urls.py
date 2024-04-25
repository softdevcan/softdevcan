# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),  # Ana sayfa
    path('<int:pk>/', views.blog_detail, name='blog_detail'),  # Gönderi detayı
]
