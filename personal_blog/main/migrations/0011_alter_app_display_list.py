# Generated by Django 3.2.5 on 2021-08-11 06:45

from django.db import models
from django.db.models import JSONField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210811_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='display_list',
            field=models.JSONField(blank=True,null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='display_list',
            field=models.JSONField(blank=True,null=True),
        )
    ]
