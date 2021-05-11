from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APIClient

from api import serializers
from core import models



STANDARD_VALIDATION_URL = reverse("api:standard-validation")
ADVANCED_VALIDATION_URL = reverse("api:advanced-validation")
THREEFIVER_URL = reverse("api:threefiver")

def sample_superuser():
    user = get_user_model().objects.create_superuser(
        username="superuser",
        email="superuser@gmail.com",
        password="test1234",
    )
    return user

def sample_postcode():
    payload = {"postcode": "Test",
                "lat": "232",
                "long": "123",
                "county": "test",
                "district": "test",
                "ward": "test ok",
                "constituency": "test",
               }


    postcode = models.PostcodeModel.objects.create(**payload)
    return postcode


class StandardValidationApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = sample_superuser()
        self.postcode = sample_postcode()



    def test_get_standard_validation_view(self):

        self.client.force_authenticate(self.superuser)
        response = self.client.get(STANDARD_VALIDATION_URL,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_validate_incorrect_postcode(self):

        self.client.force_authenticate(self.superuser)
        payload = {'postcode': '123 456'}
        response = self.client.post(STANDARD_VALIDATION_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['result']), "Invalid")


    def test_validate_correct_postcode(self):

        self.client.force_authenticate(self.superuser)
        payload = {'postcode': 'BD177JW'}
        response = self.client.post(STANDARD_VALIDATION_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['result']), "Valid")


class AdvancedValidationApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = sample_superuser()
        self.postcode = sample_postcode()



    def test_get_advanced_validation_view(self):

        self.client.force_authenticate(self.superuser)
        response = self.client.get(ADVANCED_VALIDATION_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_validate_incorrect_postcode(self):

        self.client.force_authenticate(self.superuser)
        payload = {'postcode': '123 456'}
        response = self.client.post(ADVANCED_VALIDATION_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['result']), "Invalid")


    def test_validate_correct_postcode(self):

        self.client.force_authenticate(self.superuser)
        payload = {'postcode': 'Test'}
        response = self.client.post(ADVANCED_VALIDATION_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 8)

class ThreeFiverApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = sample_superuser()


    def test_get_threefiver_view(self):

        self.client.force_authenticate(self.superuser)
        response = self.client.get(THREEFIVER_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['numbers']), 100)