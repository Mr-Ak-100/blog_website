from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=30, verbose_name="Display Name", primary_key=True)
    sidebar = models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sidebar"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

