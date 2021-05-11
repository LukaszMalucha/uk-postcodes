from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from core import models

DB_MANAGER_URL = reverse("db_manager:db-manager")
POSTCODE_UPLOAD_URL = reverse("db_manager:postcode-upload")

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

class DBManagerViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = sample_superuser()
        self.sample_postcode = sample_postcode()

    def test_retrieve_db_manager(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(DB_MANAGER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "db-manager.html")


    def test_retrieve_upload_postcode_view(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(POSTCODE_UPLOAD_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "postcode-upload.html")