from django.contrib import admin
from . models import Message, Info, Social, Log

admin.site.register(Message)
admin.site.register(Info)
admin.site.register(Social)
admin.site.register(Log)
