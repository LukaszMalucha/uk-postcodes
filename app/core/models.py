from django.db import models


class PostcodeModel(models.Model):
    """Model for uk postcode"""
    postcode = models.CharField(max_length=254, unique=True)
    lat = models.CharField(max_length=254, blank=True)
    long = models.CharField(max_length=254, blank=True)
    county = models.CharField(max_length=254, blank=True)
    district = models.CharField(max_length=254, blank=True)
    ward = models.CharField(max_length=254, blank=True)
    constituency = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f"{self.postcode}"
