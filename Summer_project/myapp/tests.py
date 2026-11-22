from django.test import TestCase
from django.urls import reverse
from .models import UserProfile


class HomeViewTest(TestCase):
    def test_get_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/home.html')

    def test_post_valid_name(self):
        response = self.client.post(reverse('home'), {'name': 'Алия'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserProfile.objects.filter(name='Алия').exists())

    def test_post_empty_name(self):
        response = self.client.post(reverse('home'), {'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(UserProfile.objects.exists())
