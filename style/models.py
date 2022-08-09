from django.db import models
from core.models import TimeStampedModel
from products.models import Product
from users.models import User


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to="product/%Y/%m/%d/")
    product = models.ForeignKey("Post", on_delete=models.CASCADE)


class Post(TimeStampedModel):
    users = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.users}의 STYLE"

    comment = models.TextField(verbose_name="내용", max_length=1000)

    products = models.ManyToManyField(Product, related_name="products")

    def count_style(self):
        return self.products.count()

    count_style.short_description = "상품태그 수"

    class Meta:
        verbose_name_plural = "스타일"
