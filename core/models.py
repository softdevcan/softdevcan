from django.core.validators import MaxValueValidator, MinValueValidator
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
        'next.js': '<i class="devicon-nextjs-line"></i>',

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
        'claude': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 509.64" width="1em" height="1em"><path fill="#D77655" d="M115.612 0h280.775C459.974 0 512 52.026 512 115.612v278.415c0 63.587-52.026 115.612-115.613 115.612H115.612C52.026 509.639 0 457.614 0 394.027V115.612C0 52.026 52.026 0 115.612 0z"/><path fill="#FCF2EE" fill-rule="nonzero" d="M142.27 316.619l73.655-41.326 1.238-3.589-1.238-1.996-3.589-.001-12.31-.759-42.084-1.138-36.498-1.516-35.361-1.896-8.897-1.895-8.34-10.995.859-5.484 7.482-5.03 10.717.935 23.683 1.617 35.537 2.452 25.782 1.517 38.193 3.968h6.064l.86-2.451-2.073-1.517-1.618-1.517-36.776-24.922-39.81-26.338-20.852-15.166-11.273-7.683-5.687-7.204-2.451-15.721 10.237-11.273 13.75.935 3.513.936 13.928 10.716 29.749 23.027 38.848 28.612 5.687 4.727 2.275-1.617.278-1.138-2.553-4.271-21.13-38.193-22.546-38.848-10.035-16.101-2.654-9.655c-.935-3.968-1.617-7.304-1.617-11.374l11.652-15.823 6.445-2.073 15.545 2.073 6.547 5.687 9.655 22.092 15.646 34.78 24.265 47.291 7.103 14.028 3.791 12.992 1.416 3.968 2.449-.001v-2.275l1.997-26.641 3.69-32.707 3.589-42.084 1.239-11.854 5.863-14.206 11.652-7.683 9.099 4.348 7.482 10.716-1.036 6.926-4.449 28.915-8.72 45.294-5.687 30.331h3.313l3.792-3.791 15.342-20.372 25.782-32.227 11.374-12.789 13.27-14.129 8.517-6.724 16.1-.001 11.854 17.617-5.307 18.199-16.581 21.029-13.75 17.819-19.716 26.54-12.309 21.231 1.138 1.694 2.932-.278 44.536-9.479 24.062-4.347 28.714-4.928 12.992 6.066 1.416 6.167-5.106 12.613-30.71 7.583-36.018 7.204-53.636 12.689-.657.48.758.935 24.164 2.275 10.337.556h25.301l47.114 3.514 12.309 8.139 7.381 9.959-1.238 7.583-18.957 9.655-25.579-6.066-59.702-14.205-20.474-5.106-2.83-.001v1.694l17.061 16.682 31.266 28.233 39.152 36.397 1.997 8.999-5.03 7.102-5.307-.758-34.401-25.883-13.27-11.651-30.053-25.302-1.996-.001v2.654l6.926 10.136 36.574 54.975 1.895 16.859-2.653 5.485-9.479 3.311-10.414-1.895-21.408-30.054-22.092-33.844-17.819-30.331-2.173 1.238-10.515 113.261-4.929 5.788-11.374 4.348-9.478-7.204-5.03-11.652 5.03-23.027 6.066-30.052 4.928-23.886 4.449-29.674 2.654-9.858-.177-.657-2.173.278-22.37 30.71-34.021 45.977-26.919 28.815-6.445 2.553-11.173-5.789 1.037-10.337 6.243-9.2 37.257-47.392 22.47-29.371 14.508-16.961-.101-2.451h-.859l-98.954 64.251-17.618 2.275-7.583-7.103.936-11.652 3.589-3.791 29.749-20.474z"/></svg>',
        'cursor': '<svg role="img" viewBox="0 0 24 24" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23"/></svg>',
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
        ordering = ('-percentage', 'name')

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
        return f'{self.get_platform_display()}: {self.link}'  # type: ignore[attr-defined]

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
