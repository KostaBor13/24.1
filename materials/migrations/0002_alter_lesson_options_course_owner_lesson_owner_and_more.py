# Generated by Django 5.0.6 on 2024-07-03 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lesson",
            options={"verbose_name": "урок", "verbose_name_plural": "уроки"},
        ),
        migrations.AddField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="введите описание курса",
                null=True,
                verbose_name="описание курса",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="выберите изображение",
                null=True,
                upload_to="materials/course",
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(
                help_text="введите название курса",
                max_length=100,
                verbose_name="название курса",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                help_text="выберите курс",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lesson_set",
                to="materials.course",
                verbose_name="курс",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="введите описание",
                null=True,
                verbose_name="описание урока",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="выберите изображение",
                null=True,
                upload_to="materials/lesson",
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="name",
            field=models.CharField(
                help_text="введите название",
                max_length=100,
                verbose_name="название урока",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="добавьте ссылку",
                null=True,
                verbose_name="ссылка",
            ),
        ),
    ]