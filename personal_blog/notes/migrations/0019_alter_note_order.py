# Generated by Django 3.2.6 on 2021-09-16 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0018_alter_note_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
