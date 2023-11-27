from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jalali_models


choices = (("Login", "Login"), ("Register", "Register"), ("Logout", "Logout"))


class AuthenticationLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authentication_log", null=True,
                             verbose_name="حساب کاربری")
    type = models.CharField(choices=choices, max_length=20, verbose_name="نوع")
    client_ip = models.GenericIPAddressField(verbose_name="IP")
    device = models.CharField(max_length=40, verbose_name="دستگاه")
    os = models.CharField(max_length=40, verbose_name="سیستم عامل")
    os_version = models.CharField(max_length=20, verbose_name="نسخه سیستم عامل")
    browser = models.CharField(max_length=40, verbose_name="مرورگر")
    browser_version = models.CharField(max_length=20, verbose_name="نسخه مرورگر")
    created = jalali_models.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "لاگ"
        verbose_name_plural = "لاگ ها"

    def __str__(self):

        return f"{self.type} confirmed by {self.user.username} in {self.created.date()}"
