from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.
class AuthenticationTests(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

    def test_profile_update(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('profile'), {
            'bio': 'Updated bio'
        })
        user.refresh_from_db()
        self.assertEqual(user.userprofile.bio, 'Updated bio')

