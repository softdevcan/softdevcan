from django.urls import path, include
from .views import index, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('blog/', include('blog.urls')),
    path('<slug>/', redirect_urls, name='redirect_urls'),
]
