# Generated by Django 3.2.4 on 2021-06-10 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20210610_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AlterField(
            model_name='note',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
