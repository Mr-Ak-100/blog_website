# Generated by Django 4.2.4 on 2023-11-26 23:58

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_authenticationlog_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticationlog',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]
