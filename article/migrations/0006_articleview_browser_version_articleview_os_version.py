# Generated by Django 4.2.4 on 2023-08-12 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articleview'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleview',
            name='browser_version',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleview',
            name='os_version',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
