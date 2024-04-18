from django.shortcuts import render, get_object_or_404, redirect
from core.models import GeneralSettings, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.
def layout(request):
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

    documents = Document.objects.all()
    social_medias = SocialMedia.objects.all()
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
        'documents': documents,
        'social_medias': social_medias,
    }
    return context
def index(request):
    # Skills
    skills = Skill.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    context = {

        'skills': skills,
        'experiences': experiences,
        'educations': educations,

    }
    return render(request, 'index.html', context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)