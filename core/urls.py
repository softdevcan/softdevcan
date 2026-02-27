from django.urls import include, path

from .views import index, portfolio, project_detail, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', project_detail, name='project_detail'),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('<slug>/', redirect_urls, name='redirect_urls'),
]
