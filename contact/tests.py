from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Message


class ContactFormTest(TestCase):
    def test_valid_form(self):
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_email(self):
        form = ContactForm(data={
            'name': 'Test User',
            'subject': 'Test Subject',
            'message': 'Test message content',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_invalid_form_bad_email(self):
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'not-an-email',
            'subject': 'Test Subject',
            'message': 'Test message content',
        })
        self.assertFalse(form.is_valid())


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    @patch('contact.forms.EmailMessage.send')
    def test_contact_form_post_valid(self, mock_send):
        mock_send.return_value = 1
        response = self.client.post(reverse('contact_form'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content',
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(Message.objects.count(), 1)
        mock_send.assert_called_once()

    def test_contact_form_get_returns_error(self):
        response = self.client.get(reverse('contact_form'))
        data = response.json()
        self.assertFalse(data['success'])
