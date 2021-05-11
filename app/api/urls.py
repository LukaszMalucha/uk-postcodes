from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


app_name = "api"


router = DefaultRouter()
router.register("postcodes", views.PostcodeModelViewSet, basename="postcodes")

urlpatterns = [
    path("", include(router.urls)),
    path("standard-validation/", views.StandardValidationView.as_view(), name="standard-validation"),
    path("advanced-validation/", views.AdvancedValidationView.as_view(), name="advanced-validation"),
]













