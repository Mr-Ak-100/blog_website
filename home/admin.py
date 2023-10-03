from django.contrib import admin
from . models import Message, Info, Social, Log
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Info)
class InfoAdmin(SummernoteModelAdmin):

    summernote_fields = ("main_text", "about_text")


admin.site.register(Message)
admin.site.register(Social)
admin.site.register(Log)
