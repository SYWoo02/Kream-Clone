from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    filter_horizontal = ("products",)
    list_display = ("__str__", "count_products")
