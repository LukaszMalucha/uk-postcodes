from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APIClient

from api import serializers
from core import models



CURRENT_USER_URL = reverse("user:current-user")


def sample_superuser():
    user = get_user_model().objects.create_superuser(
        username="superuser",
        email="superuser@gmail.com",
        password="test1234",
    )
    return user


class CurrentUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = sample_superuser()



    def test_get_current_user_view(self):

        self.client.force_authenticate(self.superuser)
        response = self.client.get(CURRENT_USER_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['admin'], True)


