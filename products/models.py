from unicodedata import name
from django.db import models
from core.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "브랜드"


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to="product/%Y/%m/%d/")

    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "이미지"


class Product(TimeStampedModel):
    eng_name = models.CharField(max_length=150, verbose_name="영어 이름")
    kor_name = models.CharField(max_length=150, verbose_name="한글 이름")
    model_number = models.CharField(max_length=80, verbose_name="모델 번호")
    released = models.DateField(
        verbose_name="발매일",
    )
    color = models.CharField(max_length=120, verbose_name="색상")
    released_price = models.PositiveIntegerField(
        verbose_name="발매가",
    )
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name="브랜드명")
    # foreignKey필드는 1:多 관계를 나타내는 필드

    def __str__(self) -> str:
        # return f"{self.brand} _ {self.eng_name}"
        return self.eng_name

    class Meta:
        verbose_name_plural = "상품"
        ordering = ["eng_name", "updated"]
