# Generated by Django 3.2.6 on 2021-10-04 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0019_alter_note_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['order']},
        ),
    ]
