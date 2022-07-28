from django.contrib import admin
from .models import Brand, Photo, Product


# Register your models here.
class PhotoInLine(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine]
    list_display = ("brand", "eng_name", "kor_name")
    search_fields = ("eng_name", "kor_name", "brand__name")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ("brand__name",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
