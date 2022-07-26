from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SHOES_SIZE_CHOICES = [
        ("220", "220"),
        ("225", "225"),
        ("230", "230"),
        ("235", "235"),
        ("240", "240"),
        ("245", "245"),
        ("250", "250"),
        ("255", "255"),
        ("260", "260"),
        ("265", "265"),
        ("270", "270"),
        ("275", "275"),
        ("280", "280"),
        ("285", "285"),
        ("290", "290"),
        ("295", "295"),
        ("300", "300"),
    ]
    avatar = models.ImageField(verbose_name="프로필 이미지", blank=True, null=True)
    phone_number = models.CharField(verbose_name="연락처", max_length=11)
    shoes_size = models.CharField(
        verbose_name="신발 사이즈", choices=SHOES_SIZE_CHOICES, max_length=3, blank=True
    )
    is_ad_message = models.BooleanField(verbose_name="광고성 메세지 수신동의 여부", default=False)
    is_ad_email = models.BooleanField(verbose_name="광고성 이메일 수신동의 여부", default=False)


# Create your models here.
