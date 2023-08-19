from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed


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
    website_title = models.CharField(max_length=35)
    website_logo = models.ImageField(upload_to="main_images")
    phone = models.IntegerField()
    email = models.EmailField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    about_text = models.TextField()
    main_logo = models.ImageField(upload_to="main_images")
    about_image = models.ImageField(upload_to="main_images")

    def save(self, *args, **kwargs):

        query = Info.objects.all()

        if self.id:
            count = query.exclude(id=self.id).count()
        else:
            count = query.count()

        if count >= 1:
            return HttpResponseNotAllowed("Only one Info")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Info"

    def __str__(self):
        return "Info"


class Social(models.Model):

    facebook = models.URLField(default="https://facebook.com")
    twitter = models.URLField(default="https://twitter.com")
    instagram = models.URLField(default="https://www.instagram.com/")
    pinterest = models.URLField(default="https://www.pinterest.com/")
    youtube = models.URLField(default="https://youtube.com/")

    def save(self, *args, **kwargs):

        query = Social.objects.all()

        if self.id:
            count = query.exclude(id=self.id).count()
        else:
            count = query.count()

        if count >= 1:
            return HttpResponseNotAllowed("Only one Social")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Social"

    def __str__(self):
        return "Social"


class Log(models.Model):

    page = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_log", null=True)
    client_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=40)
    os = models.CharField(max_length=40)
    os_version = models.CharField(max_length=20)
    browser = models.CharField(max_length=40)
    browser_version = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.page} requested by {self.client_ip}"
