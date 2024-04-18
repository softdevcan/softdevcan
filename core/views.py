from django.shortcuts import render
from core.models import GeneralSettings, ImageSetting
# Create your views here.

def index(request):
    site_title = GeneralSettings.objects.get(name='site_title').parameter
    site_keywords = GeneralSettings.objects.get(name='site_keywords').parameter
    site_description = GeneralSettings.objects.get(name='site_description').parameter
    home_banner_name = GeneralSettings.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSettings.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSettings.objects.get(name='home_banner_description').parameter
    about_myself_footer = GeneralSettings.objects.get(name='about_myself_footer').parameter
    about_myself_welcome = GeneralSettings.objects.get(name='about_myself_welcome').parameter

    # Images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
    }
    return render(request, 'index.html', context=context)