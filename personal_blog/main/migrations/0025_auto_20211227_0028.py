# Generated by Django 3.2.6 on 2021-12-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_setting_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='app_display_dict',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='todos',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
