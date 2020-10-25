# Generated by Django 3.1.2 on 2020-10-25 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0002_auto_20201019_0649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='clips',
            options={'verbose_name': 'Клип', 'verbose_name_plural': 'Клипы'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
        migrations.RemoveField(
            model_name='album',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='clips',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='song',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='clips',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.album'),
        ),
    ]