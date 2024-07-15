from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}
METHOD_CHOICES = [
    ('Cash', 'Наличные'),
    ('Non-cash', 'Безнал'),
]


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="email",
        help_text="Email address"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        help_text="номер телефона",
        **NULLABLE
    )
    city = models.CharField(
        max_length=200,
        verbose_name="город",
        help_text="ваш город",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="ваш аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payment(models.Model):
    """Модель оплаты"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_payment',
        verbose_name='пользователь',
        help_text='выберите пользователя',


    )
    date_of_payment = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата оплаты'
    )

    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='оплаченный курс',
        **NULLABLE,
        related_name='paid_course_payments'
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name='оплаченный урок',
        **NULLABLE,
        related_name='paid_lesson_payments'
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name='сумма оплаты',
        help_text='введите сумму оплаты',


    )
    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES,
        verbose_name='способ оплаты',
        help_text='выберите способ оплаты'
    )

    payment_link = models.URLField(
        max_length=400,
        verbose_name='ссылка на оплату',
        **NULLABLE
    )
    payment_status = models.CharField(
        max_length=30,
        verbose_name='статус платежа',
        **NULLABLE
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name='id сессии',
        **NULLABLE
    )


    def clean(self):
        if self.paid_course and self.paid_lesson:
            raise ValidationError('Оплата может быть связана только с курсом или уроком, но не с обоими.')
        if not self.paid_course and not self.paid_lesson:
            raise ValidationError('Одно из полей "курс" или "урок" должно быть заполнено.')
        super().clean()

    def __str__(self):
        return f'''{self.user}: {self.date_of_payment}, {self.payment_amount}, {self.payment_method}
{self.paid_course if self.paid_course else self.paid_lesson}'''

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"