# Generated by Django 3.2.4 on 2021-06-24 18:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_uuid_chapter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
