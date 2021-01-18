from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = '/api/create/'
PROFILE_URL = '/api/profile/'
TOKEN_URL = '/api/auth/'


class AuthorizedUserApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='dummy',
            password='dummy_pw'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_1_should_get_user_profile(self):
        res = self.client.get(PROFILE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'id': self.user.id,
            'username': self.user.username
        })

    def test_2_should_not_allowed_by_PUT(self):
        payload = {
            'username': 'dummy',
            'password': 'dummy_ps'
        }
        res = self.client.put(PROFILE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_3_should_not_allowed_by_PATCH(self):
        payload = {
            'username': 'dummy',
            'password': 'dummy_ps'
        }
        res = self.client.patch(PROFILE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
