from django.urls import path
from . import views


app_name = "article"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("<slug:category_slug>", views.category, name="category")
]
