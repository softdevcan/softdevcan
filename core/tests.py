from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from core.models import (
    GeneralSetting, ImageSetting, Skill, Experience, Education,
    SocialMedia, Document, Project, ProjectCategory,
)
from core.views import get_general_setting, get_image_setting


class GeneralSettingModelTest(TestCase):
    def test_create_and_retrieve(self):
        GeneralSetting.objects.create(name='site_title', parameter='Test Site')
        setting = GeneralSetting.objects.get(name='site_title')
        self.assertEqual(setting.parameter, 'Test Site')

    def test_get_general_setting_found(self):
        GeneralSetting.objects.create(name='site_title', parameter='My Site')
        result = get_general_setting('site_title')
        self.assertEqual(result, 'My Site')

    def test_get_general_setting_not_found(self):
        result = get_general_setting('nonexistent')
        self.assertEqual(result, '')


class ImageSettingModelTest(TestCase):
    def test_get_image_setting_not_found(self):
        result = get_image_setting('nonexistent')
        self.assertEqual(result, '')


class SkillModelTest(TestCase):
    def test_ordering_by_order_field(self):
        Skill.objects.create(name='Python', order=2, skill_type='backend')
        Skill.objects.create(name='Django', order=1, skill_type='backend')
        Skill.objects.create(name='React', order=3, skill_type='frontend')
        skills = list(Skill.objects.values_list('name', flat=True))
        self.assertEqual(skills, ['Django', 'Python', 'React'])

    def test_percentage_validators(self):
        skill = Skill(name='Test', percentage=150, skill_type='backend')
        with self.assertRaises(ValidationError):
            skill.full_clean()

        skill_neg = Skill(name='Test', percentage=-10, skill_type='backend')
        with self.assertRaises(ValidationError):
            skill_neg.full_clean()


class ProjectModelTest(TestCase):
    def test_auto_slug_generation(self):
        project = Project.objects.create(
            title='My Test Project',
            description='A test project',
        )
        self.assertEqual(project.slug, 'my-test-project')

    def test_get_technologies_list(self):
        project = Project.objects.create(
            title='Tech Project',
            description='Test',
            technologies='Django, React, PostgreSQL',
        )
        self.assertEqual(
            project.get_technologies_list(),
            ['Django', 'React', 'PostgreSQL'],
        )

    def test_empty_technologies_list(self):
        project = Project.objects.create(
            title='No Tech',
            description='Test',
        )
        self.assertEqual(project.get_technologies_list(), [])


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_contains_skills(self):
        Skill.objects.create(name='Python', order=1, skill_type='backend')
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Python')


class PortfolioViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = ProjectCategory.objects.create(name='Web', slug='web')
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project',
            category=self.category,
            is_published=True,
        )

    def test_portfolio_page_loads(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)

    def test_portfolio_category_filter(self):
        response = self.client.get(reverse('portfolio') + '?category=web')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_project_detail_page(self):
        response = self.client.get(
            reverse('project_detail', kwargs={'slug': self.project.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_unpublished_project_returns_404(self):
        self.project.is_published = False
        self.project.save()
        response = self.client.get(
            reverse('project_detail', kwargs={'slug': self.project.slug})
        )
        self.assertEqual(response.status_code, 404)


class LayoutContextProcessorTest(TestCase):
    def test_context_contains_site_title(self):
        GeneralSetting.objects.create(name='site_title', parameter='My Portfolio')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['site_title'], 'My Portfolio')

    def test_context_with_missing_settings(self):
        """Empty DB should not crash - defaults to empty string"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['site_title'], '')
