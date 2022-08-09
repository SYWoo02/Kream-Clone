from re import U
from django.contrib import admin

from products.admin import PhotoInLine
from products.models import Photo
from .models import Post, Photo

class PhotoInLine(admin.StackedInline):
    model = Photo
    extra = 5

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine]
    filter_horizontal = ("products",)
    list_display = ("__str__", "count_style")
