from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from django_jalali.db import models as jalali_models


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="messages", null=True, blank=True, verbose_name="نویسنده")
    name = models.CharField(max_length=50, null=True, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    title = models.CharField(max_length=150, verbose_name="موضوع")
    body = models.TextField(verbose_name="متن پیام")
    created = jalali_models.jDateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, verbose_name="خوانده شده ؟")

    class Meta:
        ordering = ["read", "-created"]
        verbose_name = "پیام کاربر"
        verbose_name_plural = "پیام های کاربران"

    def __str__(self):
        if self.user is not None:
            return f" {self.read} | {self.user.username} > {self.title[:30]}"
        else:
            return f" {self.read} | {self.name} > {self.title[:30]}"


class Info(models.Model):

    main_text = models.TextField(max_length=150, verbose_name="متن کوتاه سایدبار")
    website_title = models.CharField(max_length=35)
    website_logo = models.ImageField(upload_to="main_images", verbose_name="لوگو 1")
    phone = models.IntegerField(verbose_name="شماره موبایل")
    email = models.EmailField(verbose_name="ایمیل")
    country = models.CharField(max_length=20, verbose_name="کشکور")
    city = models.CharField(max_length=20, verbose_name="شهر")
    about_text = models.TextField(verbose_name="متن صفحه درباره ما")
    main_logo = models.ImageField(upload_to="main_images", verbose_name="لوگو اصلی")
    about_image = models.ImageField(upload_to="main_images", verbose_name="تصویر صفحه درباره ما")

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
        verbose_name = "اطلاعات اصلی"
        verbose_name_plural = "اطلاعات اصلی"

    def __str__(self):
        return "اطلاعات"


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
        verbose_name = "شبکه های اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

    def __str__(self):
        return "شبکه های اجتماعی"


class Log(models.Model):

    page = models.CharField(max_length=40, verbose_name="صفحه بازدید شده")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_log", null=True, verbose_name="حساب کاربری")
    client_ip = models.GenericIPAddressField(verbose_name="IP")
    device = models.CharField(max_length=40, verbose_name="دستگاه")
    os = models.CharField(max_length=40, verbose_name="سیستم عامل")
    os_version = models.CharField(max_length=20, verbose_name="نسخه سیستم عامل")
    browser = models.CharField(max_length=40, verbose_name="مرورگر")
    browser_version = models.CharField(max_length=20, verbose_name="نسخه مرورگر")
    created = jalali_models.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "لاگ"
        verbose_name_plural = "لاگ ها"

    def __str__(self):

        if self.user:
            return f"{self.page} requested by {self.user.username}"

        else:
            return f"{self.page} requested by {self.client_ip}"
        