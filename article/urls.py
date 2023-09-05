from django.urls import path
from . import views


app_name = "article"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("d/<slug:article_slug>", views.detail, name="detail"),
    path("search", views.search, name="search"),
    path("<slug:category_slug>", views.category, name="category"),
]
