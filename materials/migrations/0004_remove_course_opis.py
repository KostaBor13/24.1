# Generated by Django 5.0.6 on 2024-07-13 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_course_opis"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="opis",
        ),
    ]