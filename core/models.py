from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated Date',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created Date',
    )
    class Meta:
        abstract = True
class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='Name of the setting',
    )
    description = models.TextField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='Description of the setting',
    )
    parameter = models.TextField(
        default='',
        max_length=1024,
        blank=True,
        verbose_name='Parameter',
        help_text='Parameter of the setting',
    )
    def __str__(self):
        return f"General Settings: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']

class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='image_settings/',
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    SKILL_TYPE_CHOICES = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    )
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPE_CHOICES, default='backend')

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)

class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('start_date',)

class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )
    major = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('start_date',)

class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)

class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
        help_text='',
    )
    file = models.FileField(
        default='',
        verbose_name='File',
        help_text='',
        blank=True,
        upload_to='documents/',
    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)


class ProjectCategory(AbstractModel):
    """Category for portfolio projects"""
    name = models.CharField(max_length=100, verbose_name='Category Name')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    order = models.IntegerField(default=0, verbose_name='Order')

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
        ordering = ('order', 'name')


class Project(AbstractModel):
    """Portfolio project model"""
    title = models.CharField(max_length=200, verbose_name='Project Title')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(verbose_name='Short Description')
    content = models.TextField(blank=True, verbose_name='Detailed Content (Markdown)')

    # Media
    featured_image = models.ImageField(
        upload_to='projects/',
        blank=True,
        verbose_name='Featured Image'
    )

    # Categorization
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )

    # Links
    github_url = models.URLField(blank=True, verbose_name='GitHub URL')
    live_url = models.URLField(blank=True, verbose_name='Live Demo URL')

    # Technologies used
    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text='Comma-separated list of technologies (e.g., Django, React, PostgreSQL)'
    )

    # Display settings
    is_featured = models.BooleanField(default=False, verbose_name='Featured Project')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_technologies_list(self):
        """Return technologies as a list"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('order', '-created_date')