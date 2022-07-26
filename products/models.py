from django.db import models
from core.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(max_length=50)


class Photo(TimeStampedModel):
    image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Product(TimeStampedModel):
    eng_name = models.CharField(max_length=150)
    kor_name = models.CharField(max_length=150)
    model_number = models.CharField(max_length=80)
    released = models.DateField()
    color = models.CharField(max_length=120)
    released_price = models.PositiveIntegerField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    # foreignKey필드는 1:多 관계를 나타내는 필드
