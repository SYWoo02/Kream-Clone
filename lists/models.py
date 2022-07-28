from django.db import models
from core.models import TimeStampedModel


class List(TimeStampedModel):
    """관심상품 모델에 대한 정의"""

    products = models.ManyToManyField(
        "products.Product", related_name="lists"
    )  # 多:多 관계
    users = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE
    )
    # 유저는 장바구니를 하나만 들고다닌다

    def __str__(self) -> str:
        return f"{self.users}의 관심상품"

    def count_products(self):
        return self.products.count()

    count_products.short_description = "상품 수"

    class Meta:
        verbose_name_plural = "관심상품"
