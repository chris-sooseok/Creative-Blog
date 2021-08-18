# Generated by Django 3.2.6 on 2021-08-16 10:51

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_setting_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=90, size=[128, 128], upload_to='profile_pic/'),
        ),
    ]
