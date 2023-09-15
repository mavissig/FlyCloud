from django.test import TestCase, Client
from django.contrib.auth.models import User


class AuthorizationUserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')

    def test_authorization_success(self):
        c = Client()
        response = c.post('', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('message'), 'Authorized')

    def test_authorization_failure_wrong_password(self):
        c = Client()
        response = c.post('', {'username': 'admin', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json().get('message'), 'Unauthorized')

    def test_authorization_failure_user_not_found(self):
        c = Client()
        response = c.post('auth/', {'username': 'nonexistent_user', 'password': 'password'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('error'), 'User not found')

    def test_invalid_http_method(self):
        c = Client()
        response = c.get('/auth/')  # Using GET instead of POST
        self.assertEqual(response.status_code, 405)
