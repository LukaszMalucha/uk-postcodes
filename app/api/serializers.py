from rest_framework import serializers

from core import models




class PostcodeModelSerializer(serializers.ModelSerializer):
    """Serializer for postcode"""

    class Meta:
        model = models.PostcodeModel
        fields = "__all__"
        read_only_fields = ("id",)


