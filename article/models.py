from django.db import models
from django.contrib.auth.models import User
from . managers import CategoryManager, ArticleManager


class Category(models.Model):

    title = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=30, verbose_name="Display Name", primary_key=True)
    sidebar = models.BooleanField(default=False, help_text="show in sidebar")
    created = models.DateTimeField(auto_now_add=True)
    objects = CategoryManager()

    class Meta:
        ordering = ["-sidebar"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=30, verbose_name="Display Name", primary_key=True)
    main_image = models.ImageField(upload_to="articles_images/")
    body = models.TextField()

    views = models.IntegerField(default=0)
    banner = models.BooleanField(default=False, verbose_name="Home Banner", help_text="show in home banners")
    home_item = models.BooleanField(default=False, help_text="show in home page articles")
    published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ArticleManager()

    def __str__(self):
        return f"{self.author.username} > {self.title[:40]}"
