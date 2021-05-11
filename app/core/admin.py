from django.contrib import admin
from core.models import PostcodeModel


class PostcodeModelAdmin(admin.ModelAdmin):
    list_display = ["postcode", "county", "district", "ward", "constituency"]

    class Meta:
        model = PostcodeModel


admin.site.register(PostcodeModel, PostcodeModelAdmin)
