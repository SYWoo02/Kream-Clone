from django.urls import path
from . import views

app_name = "styles"

urlpatterns = [
    path("", views.StyleListView.as_view(), name="list"),
    path("<int:st>", views.StyleDetail.as_view(), name="detail"),
]
