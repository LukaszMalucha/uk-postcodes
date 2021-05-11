from django.urls import path, include
from db_manager.views import db_manager, postcode_upload

app_name = "db_manager"

urlpatterns = [
    path("", db_manager, name="db-manager"),
    path("postcode-upload", postcode_upload, name="postcode-upload"),
]