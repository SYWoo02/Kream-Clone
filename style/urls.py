from django.urls import path
from . import views

app_name = "styles"

urlpatterns = [
    path("", views.StyleListView.as_view(), name="list"),
    path("<int:pk>", views.StyleDetail.as_view(), name="detail"),
]
