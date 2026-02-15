from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.decorators import display
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document, ProjectCategory, Project


@admin.register(GeneralSetting)
class GeneralSettingAdmin(ModelAdmin):
    """General site settings with modern UI"""
    list_display = ('name', 'description', 'parameter_preview', 'updated_date')
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'parameter')
    list_per_page = 20

    @display(description=_("Parameter"))
    def parameter_preview(self, obj):
        """Show parameter preview (truncated)"""
        if len(obj.parameter) > 50:
            return format_html('<span title="{}">{}</span>', obj.parameter, obj.parameter[:50] + '...')
        return obj.parameter


@admin.register(ImageSetting)
class ImageSettingAdmin(ModelAdmin):
    """Image settings with preview"""
    list_display = ('name', 'description', 'image_preview', 'updated_date')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 20

    @display(description=_("Preview"))
    def image_preview(self, obj):
        """Show image thumbnail"""
        if obj.file:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 100px; border-radius: 4px;" />', obj.file.url)
        return '-'


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    """Skills with icon preview and percentage bar"""
    list_display = ('order', 'name', 'icon_preview', 'skill_type', 'percentage_bar', 'updated_date')
    list_display_links = ('name',)
    list_filter = ('skill_type',)
    search_fields = ('name',)
    list_per_page = 20

    @display(description=_("Icon"))
    def icon_preview(self, obj):
        """Show skill icon"""
        return format_html('<span style="font-size: 20px;">{}</span>', obj.get_icon())

    @display(description=_("Level"), ordering="percentage")
    def percentage_bar(self, obj):
        """Show percentage as progress bar"""
        color = '#059669' if obj.percentage >= 70 else '#F59E0B' if obj.percentage >= 50 else '#EF4444'
        return format_html(
            '<div style="width: 100px; background: #E5E7EB; border-radius: 4px; overflow: hidden;">'
            '<div style="width: {}%; background: {}; height: 20px; display: flex; align-items: center; justify-content: center; color: white; font-size: 11px; font-weight: 600;">'
            '{}%</div></div>',
            obj.percentage, color, obj.percentage
        )


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    """Work experience with modern layout"""
    list_display = ('company_name', 'job_title', 'job_location', 'duration_display', 'updated_date')
    list_display_links = ('company_name',)
    search_fields = ('company_name', 'job_title', 'job_location')
    list_per_page = 20

    @display(description=_("Duration"))
    def duration_display(self, obj):
        """Show work duration"""
        end = obj.end_date.strftime('%b %Y') if obj.end_date else 'Present'
        return format_html(
            '<span style="color: #6366F1;">{} - {}</span>',
            obj.start_date.strftime('%b %Y'),
            end
        )


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    """Education with modern layout"""
    list_display = ('school_name', 'major', 'department', 'duration_display', 'updated_date')
    list_display_links = ('school_name',)
    search_fields = ('school_name', 'major', 'department')
    list_per_page = 20

    @display(description=_("Duration"))
    def duration_display(self, obj):
        """Show education duration"""
        end = obj.end_date.strftime('%b %Y') if obj.end_date else 'Present'
        return format_html(
            '<span style="color: #059669;">{} - {}</span>',
            obj.start_date.strftime('%b %Y'),
            end
        )


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin):
    """Social media links with platform icons"""
    list_display = ('order', 'platform_badge', 'link_preview', 'icon_preview', 'updated_date')
    list_display_links = ('platform_badge',)
    list_filter = ('platform',)
    search_fields = ('link',)
    list_per_page = 20

    @display(description=_("Platform"), ordering="platform")
    def platform_badge(self, obj):
        """Show platform as colored badge"""
        return format_html(
            '<span style="background: #6366F1; color: white; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600;">{}</span>',
            obj.get_platform_display()
        )

    @display(description=_("Link"))
    def link_preview(self, obj):
        """Show clickable link"""
        return format_html('<a href="{}" target="_blank" style="color: #059669;">🔗 {}</a>', obj.link, obj.link[:40] + '...' if len(obj.link) > 40 else obj.link)

    @display(description=_("Icon"))
    def icon_preview(self, obj):
        """Show platform icon"""
        return format_html('<span style="font-size: 24px;">{}</span>', obj.get_icon())


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    """Documents (CV, Resume, etc.)"""
    list_display = ('order', 'slug', 'button_text', 'file_info', 'updated_date')
    list_display_links = ('slug',)
    search_fields = ('slug', 'button_text')
    list_per_page = 20

    @display(description=_("File"))
    def file_info(self, obj):
        """Show file download link"""
        if obj.file:
            return format_html('<a href="{}" target="_blank" style="color: #059669;">📄 Download</a>', obj.file.url)
        return '-'


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(ModelAdmin):
    """Project categories with project count"""
    list_display = ('order', 'name', 'slug', 'project_count')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

    @display(description=_("Projects"))
    def project_count(self, obj):
        """Show number of projects in category"""
        count = obj.projects.count()
        return format_html('<span style="color: #059669; font-weight: 600;">{} projects</span>', count)


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    """Portfolio projects with modern UI"""
    list_display = ('title', 'category', 'status_badges', 'tech_preview', 'created_date')
    list_display_links = ('title',)
    list_filter = ('category', 'is_featured', 'is_published')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category')
        }),
        (_('Content'), {
            'fields': ('description', 'content', 'featured_image'),
            'description': 'Project details and description (Markdown supported)'
        }),
        (_('Links'), {
            'fields': ('github_url', 'live_url'),
            'description': 'GitHub repository and live demo URLs'
        }),
        (_('Technologies'), {
            'fields': ('technologies',),
            'description': 'Comma-separated list (e.g., Django, React, PostgreSQL)'
        }),
        (_('Display Settings'), {
            'fields': ('is_featured', 'is_published', 'order')
        }),
    )

    @display(description=_("Status"))
    def status_badges(self, obj):
        """Show featured and published status"""
        badges = []
        if obj.is_featured:
            badges.append('<span style="background: #F59E0B; color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px; margin-right: 4px;">⭐ FEATURED</span>')
        if obj.is_published:
            badges.append('<span style="background: #059669; color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px;">✓ PUBLISHED</span>')
        else:
            badges.append('<span style="background: #6B7280; color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px;">✗ DRAFT</span>')
        return format_html(''.join(badges))

    @display(description=_("Technologies"))
    def tech_preview(self, obj):
        """Show technologies list"""
        tech_list = obj.get_technologies_list()
        if tech_list:
            preview = ', '.join(tech_list[:3])
            if len(tech_list) > 3:
                preview += f' +{len(tech_list) - 3} more'
            return format_html('<span style="color: #6366F1;">{}</span>', preview)
        return '-'