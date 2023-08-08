from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="messages", null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["read", "-created"]

    def __str__(self):
        if self.user is not None:
            return f" {self.read} | {self.user.username} > {self.title[:30]}"
        else:
            return f" {self.read} | {self.name} > {self.title[:30]}"


class Info(models.Model):

    main_text = models.TextField(max_length=150)
    phone = models.IntegerField(max_length=12)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    about_text = models.TextField()

    class Meta:
        verbose_name_plural = "Info"

    def __str__(self):
        return "Info"


class Social(models.Model):

    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Social"

    def __str__(self):
        return "Social"
