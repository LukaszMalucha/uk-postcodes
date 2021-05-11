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

def sample_restaurant():
    payload = {"name": "test",
                "cuisine": "test",
                "rating": 3,
                "price_rating": 3,
                "longitude": "322",
                "latitude": "322",
                "image": "image",
                "review": "test",
                "day": 12,
                "budget": 0,
                "link": "link",
                "active": False
               }
    restaurant = models.RestaurantModel.objects.create(**payload)
    return restaurant


class RestaurantApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = sample_superuser()
        self.restaurant = sample_restaurant()
        self.restaurant_1 = sample_restaurant()


    def test_retrieve_restaurants(self):

        self.client.force_authenticate(self.superuser)
        restaurants = models.RestaurantModel.objects.all()
        serializer = serializers.RestaurantModelSerializer(restaurants, many=True)
        response = self.client.get(RESTAURANT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
