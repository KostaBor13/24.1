from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Модель курса"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название курса',
        help_text='Введите название курса'
    )
    description = models.TextField(
        verbose_name='Описание курса',
        help_text='Описание курса',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to='materials/course',
        verbose_name='Изображение',
        help_text='Выберите изображение',
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'



class Lesson(models.Model):
    """Модель урока, параметр url это ссылка на видео урока"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название урока',
        help_text='Введите название'
    )
    description = models.TextField(
        verbose_name='Описание урока',
        help_text='Введите описание',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to='materials/lesson',
        verbose_name='Изображение',
        help_text='Выберите изображение',
        **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lesson_set',
        verbose_name='Курс',
        help_text='Выберите курс'
    )
    url = models.URLField(
        verbose_name='Ссылка',
        help_text='Добавьте ссылку',
        **NULLABLE
    )

    def __str__(self):
        return f"{self.name}, курс {self.course}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

