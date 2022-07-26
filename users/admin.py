from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(models.User)  # (models.User)
class CustomerUserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "phone_number",
                    "shoes_size",
                    "is_ad_message",
                    "is_ad_email",
                )
            },
        ),
    )
