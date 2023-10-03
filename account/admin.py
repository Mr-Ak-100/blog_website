from django.contrib import admin
from . models import AuthenticationLog


@admin.register(AuthenticationLog)
class AuthenticationLogAdmin(admin.ModelAdmin):

    list_filter = ("type",)
