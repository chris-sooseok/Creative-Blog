# Generated by Django 3.2.4 on 2021-07-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210622_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
