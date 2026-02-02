from django.urls import path, include
from .views import index, redirect_urls, portfolio, project_detail

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', project_detail, name='project_detail'),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('<slug>/', redirect_urls, name='redirect_urls'),
]
