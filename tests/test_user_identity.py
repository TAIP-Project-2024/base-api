from django.test import TestCase

# accounts/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import CustomUser


class LoginTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login')

        # Create a test user
        self.user = CustomUser.objects.create_user(
            email="user@example.com",
            password="securepassword",
            first_name="John",
            last_name="Doe",
            role="user"
        )

    def test_login_successful(self):
        response = self.client.post(self.login_url, {
            'email': 'user@example.com',
            'password': 'securepassword',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], self.user.email)

    def test_login_invalid_password(self):
        response = self.client.post(self.login_url, {
            'email': 'user@example.com',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)

    def test_login_nonexistent_user(self):
        response = self.client.post(self.login_url, {
            'email': 'nonexistent@example.com',
            'password': 'securepassword',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)

    def test_login_missing_fields(self):
        # Missing password
        response = self.client.post(self.login_url, {
            'email': 'user@example.com',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

        # Missing email
        response = self.client.post(self.login_url, {
            'password': 'securepassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

