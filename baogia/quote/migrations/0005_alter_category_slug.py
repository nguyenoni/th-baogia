# Generated by Django 3.2.9 on 2021-12-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_auto_20211201_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True, verbose_name='URL'),
        ),
    ]