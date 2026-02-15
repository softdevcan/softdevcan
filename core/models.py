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
        db_index=True,
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
        db_index=True,
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
    # Icon mapping for popular technologies (case-insensitive)
    SKILL_ICONS = {
        # Backend
        'python': '<i class="devicon-python-plain colored"></i>',
        'django': '<i class="devicon-django-plain colored"></i>',
        'flask': '<i class="devicon-flask-original colored"></i>',
        'fastapi': '<i class="devicon-fastapi-plain colored"></i>',
        'java': '<i class="devicon-java-plain colored"></i>',
        'spring': '<i class="devicon-spring-plain colored"></i>',
        'nodejs': '<i class="devicon-nodejs-plain colored"></i>',
        'node.js': '<i class="devicon-nodejs-plain colored"></i>',
        'express': '<i class="devicon-express-original colored"></i>',
        'php': '<i class="devicon-php-plain colored"></i>',
        'laravel': '<i class="devicon-laravel-plain colored"></i>',
        'ruby': '<i class="devicon-ruby-plain colored"></i>',
        'rails': '<i class="devicon-rails-plain colored"></i>',
        'go': '<i class="devicon-go-plain colored"></i>',
        'rust': '<i class="devicon-rust-plain colored"></i>',
        'c#': '<i class="devicon-csharp-plain colored"></i>',
        '.net': '<i class="devicon-dot-net-plain colored"></i>',

        # Frontend
        'html': '<i class="devicon-html5-plain colored"></i>',
        'html5': '<i class="devicon-html5-plain colored"></i>',
        'css': '<i class="devicon-css3-plain colored"></i>',
        'css3': '<i class="devicon-css3-plain colored"></i>',
        'javascript': '<i class="devicon-javascript-plain colored"></i>',
        'typescript': '<i class="devicon-typescript-plain colored"></i>',
        'react': '<i class="devicon-react-original colored"></i>',
        'vue': '<i class="devicon-vuejs-plain colored"></i>',
        'vue.js': '<i class="devicon-vuejs-plain colored"></i>',
        'angular': '<i class="devicon-angularjs-plain colored"></i>',
        'svelte': '<i class="devicon-svelte-plain colored"></i>',
        'bootstrap': '<i class="devicon-bootstrap-plain colored"></i>',
        'tailwind': '<i class="devicon-tailwindcss-plain colored"></i>',
        'jquery': '<i class="devicon-jquery-plain colored"></i>',
        'sass': '<i class="devicon-sass-original colored"></i>',
        'webpack': '<i class="devicon-webpack-plain colored"></i>',

        # Databases
        'postgresql': '<i class="devicon-postgresql-plain colored"></i>',
        'postgres': '<i class="devicon-postgresql-plain colored"></i>',
        'mysql': '<i class="devicon-mysql-plain colored"></i>',
        'mongodb': '<i class="devicon-mongodb-plain colored"></i>',
        'redis': '<i class="devicon-redis-plain colored"></i>',
        'sqlite': '<i class="devicon-sqlite-plain colored"></i>',
        'mariadb': '<i class="devicon-mysql-plain colored"></i>',
        'oracle': '<i class="devicon-oracle-original colored"></i>',

        # DevOps & Tools
        'docker': '<i class="devicon-docker-plain colored"></i>',
        'kubernetes': '<i class="devicon-kubernetes-plain colored"></i>',
        'git': '<i class="devicon-git-plain colored"></i>',
        'github': '<i class="devicon-github-original"></i>',
        'gitlab': '<i class="devicon-gitlab-plain colored"></i>',
        'jenkins': '<i class="devicon-jenkins-plain colored"></i>',
        'nginx': '<i class="devicon-nginx-original colored"></i>',
        'apache': '<i class="devicon-apache-plain colored"></i>',
        'linux': '<i class="devicon-linux-plain colored"></i>',
        'ubuntu': '<i class="devicon-ubuntu-plain colored"></i>',
        'aws': '<i class="devicon-amazonwebservices-plain-wordmark colored"></i>',
        'azure': '<i class="devicon-azure-plain colored"></i>',
        'gcp': '<i class="devicon-googlecloud-plain colored"></i>',
        'terraform': '<i class="devicon-terraform-plain colored"></i>',
        'ansible': '<i class="devicon-ansible-plain colored"></i>',

        # Other
        'graphql': '<i class="devicon-graphql-plain colored"></i>',
        'rest api': '<i class="fa-solid fa-plug"></i>',
        'api': '<i class="fa-solid fa-plug"></i>',
        'vscode': '<i class="devicon-vscode-plain colored"></i>',
        'vim': '<i class="devicon-vim-plain colored"></i>',
        'pytest': '<i class="devicon-pytest-plain colored"></i>',
        'jest': '<i class="devicon-jest-plain colored"></i>',
    }

    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='Technology/skill name (e.g., Python, Django, Docker)',
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

    def get_icon(self):
        """Return icon HTML based on skill name (case-insensitive)"""
        skill_lower = self.name.lower().strip()
        return self.SKILL_ICONS.get(skill_lower, '<i class="fa-solid fa-code"></i>')

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
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter / X'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('medium', 'Medium'),
        ('devto', 'Dev.to'),
        ('kaggle', 'Kaggle'),
        ('hackerrank', 'HackerRank'),
        ('leetcode', 'LeetCode'),
        ('codepen', 'CodePen'),
        ('stackoverflow', 'Stack Overflow'),
        ('reddit', 'Reddit'),
        ('discord', 'Discord'),
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('website', 'Personal Website'),
        ('other', 'Other'),
    ]

    PLATFORM_ICONS = {
        'github': '<i class="fa-brands fa-github"></i>',
        'linkedin': '<i class="fa-brands fa-linkedin"></i>',
        'twitter': '<i class="fa-brands fa-x-twitter"></i>',
        'instagram': '<i class="fa-brands fa-instagram"></i>',
        'facebook': '<i class="fa-brands fa-facebook"></i>',
        'youtube': '<i class="fa-brands fa-youtube"></i>',
        'medium': '<i class="fa-brands fa-medium"></i>',
        'devto': '<i class="fa-brands fa-dev"></i>',
        'kaggle': '<i class="fa-brands fa-kaggle"></i>',
        'hackerrank': '<i class="fa-brands fa-hackerrank"></i>',
        'leetcode': '<i class="fa-solid fa-code"></i>',
        'codepen': '<i class="fa-brands fa-codepen"></i>',
        'stackoverflow': '<i class="fa-brands fa-stack-overflow"></i>',
        'reddit': '<i class="fa-brands fa-reddit"></i>',
        'discord': '<i class="fa-brands fa-discord"></i>',
        'telegram': '<i class="fa-brands fa-telegram"></i>',
        'whatsapp': '<i class="fa-brands fa-whatsapp"></i>',
        'email': '<i class="fa-solid fa-envelope"></i>',
        'website': '<i class="fa-solid fa-globe"></i>',
        'other': '<i class="fa-solid fa-link"></i>',
    }

    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES,
        default='other',
        verbose_name='Platform',
        help_text='Select social media platform',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
        help_text='Full URL to your profile',
    )
    # Keep old icon field for backward compatibility
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Custom Icon (Optional)',
        help_text='Leave blank to use default platform icon',
    )

    def get_icon(self):
        """Return icon HTML - custom icon or platform default"""
        if self.icon:
            return self.icon
        return self.PLATFORM_ICONS.get(self.platform, self.PLATFORM_ICONS['other'])

    def __str__(self):
        return f'{self.get_platform_display()}: {self.link}'

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
        indexes = [
            models.Index(fields=['slug']),
        ]


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
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_published', 'order']),
        ]