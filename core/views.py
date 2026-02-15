from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document, Project, ProjectCategory


def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except Exception:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except Exception:
        obj = ''

    return obj

def layout(request):
    cached = cache.get('layout_context')
    if cached is not None:
        return cached

    # Bulk query for all general settings (2 queries instead of 12)
    general_settings = {
        gs.name: gs.parameter
        for gs in GeneralSetting.objects.filter(
            name__in=[
                'site_title', 'site_keywords', 'site_description',
                'home_banner_name', 'home_banner_title',
                'home_banner_description', 'about_myself_footer',
                'about_myself_welcome',
                'contact_email', 'contact_phone', 'contact_location',
            ]
        )
    }

    image_settings = {
        img.name: img.file
        for img in ImageSetting.objects.filter(
            name__in=['header_logo', 'home_banner_image', 'site_favicon']
        )
    }

    context = {
        'site_title': general_settings.get('site_title', ''),
        'site_keywords': general_settings.get('site_keywords', ''),
        'site_description': general_settings.get('site_description', ''),
        'home_banner_name': general_settings.get('home_banner_name', ''),
        'home_banner_title': general_settings.get('home_banner_title', ''),
        'home_banner_description': general_settings.get('home_banner_description', ''),
        'about_myself_footer': general_settings.get('about_myself_footer', ''),
        'about_myself_welcome': general_settings.get('about_myself_welcome', ''),
        'contact_email': general_settings.get('contact_email', ''),
        'contact_phone': general_settings.get('contact_phone', ''),
        'contact_location': general_settings.get('contact_location', ''),
        'header_logo': image_settings.get('header_logo', ''),
        'home_banner_image': image_settings.get('home_banner_image', ''),
        'site_favicon': image_settings.get('site_favicon', ''),
        'documents': list(Document.objects.all()),
        'social_medias': list(SocialMedia.objects.all()),
    }

    cache.set('layout_context', context, 60 * 60)  # Cache for 1 hour
    return context


@cache_page(60 * 15)  # 15 minutes
def index(request):
    # Skills
    backend_skills = Skill.objects.filter(skill_type='backend')
    frontend_skills = Skill.objects.filter(skill_type='frontend')
    devops_skills = Skill.objects.filter(skill_type='devops')
    other_skills = Skill.objects.filter(skill_type='other')
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    context = {
        'backend_skills': backend_skills,
        'frontend_skills': frontend_skills,
        'devops_skills': devops_skills,
        'other_skills': other_skills,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'index.html', context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)


@cache_page(60 * 15)  # 15 minutes
def portfolio(request):
    """Display portfolio projects with optional category filter"""
    projects = Project.objects.filter(is_published=True).select_related('category')
    categories = ProjectCategory.objects.all()

    # Category filter
    category_slug = request.GET.get('category')
    active_category = None
    if category_slug:
        active_category = get_object_or_404(ProjectCategory, slug=category_slug)
        projects = projects.filter(category=active_category)

    # Featured projects first
    featured_projects = projects.filter(is_featured=True)
    other_projects = projects.filter(is_featured=False)

    context = {
        'featured_projects': featured_projects,
        'projects': other_projects,
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'portfolio.html', context)


def project_detail(request, slug):
    """Display single project details"""
    project = get_object_or_404(
        Project.objects.select_related('category'),
        slug=slug,
        is_published=True,
    )

    # Related projects from same category
    related_projects = Project.objects.filter(
        is_published=True,
        category=project.category
    ).select_related('category').exclude(pk=project.pk)[:3] if project.category else []

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'project_detail.html', context)
