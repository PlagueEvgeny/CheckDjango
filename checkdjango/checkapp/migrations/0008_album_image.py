# Generated by Django 3.1.2 on 2020-10-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0007_auto_20201025_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=100, upload_to=None, verbose_name='Изображение'),
        ),
    ]
