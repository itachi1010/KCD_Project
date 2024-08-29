from django.test import TestCase
from django.urls import reverse
from .models import User

class UserTests(TestCase):

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'matric_number': 'A12345',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(matric_number='A12345').exists())

    def test_user_login(self):
        User.objects.create_user(matric_number='A12345', email='testuser@example.com', password='testpassword123')
        response = self.client.post(reverse('login'), {
            'matric_number': 'A12345',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)
