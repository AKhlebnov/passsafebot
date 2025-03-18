from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models

from backend.constants import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH


def validate_image_size(image):
    if image.size > 4 * 1024 * 1024:  # 4MB
        raise ValidationError("Максимальный размер файла — 4 МБ")


class User(AbstractUser):
    """Модель пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
    )
    username = models.CharField(
        verbose_name='Уникальный юзернейм',
        max_length=MAX_NAME_LENGTH,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        },
        db_index=True,
    )
    first_name = models.CharField(
        verbose_name='Имя', max_length=MAX_NAME_LENGTH,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=MAX_NAME_LENGTH,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        db_index=True,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars/',
        null=True,
        blank=True,
        default='avatars/default.png',
        validators=[validate_image_size],
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})
