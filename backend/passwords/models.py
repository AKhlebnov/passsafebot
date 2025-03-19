from django.contrib.auth import get_user_model
from django.db import models
from django_cryptography.fields import encrypt
from django.urls import reverse

from core.constants import (
    MAX_RESOURCE_LENGTH,
    MAX_ACTION_LENGTH,
    ACTION_CHOICES
)

User = get_user_model()


class AuditLog(models.Model):
    """
    Модель AuditLog для логирования.
    Поле action - Например, 'create', 'update', 'delete'.
    Поле target - Имя или ID объекта, над которым совершено действие.
    Поле timestamp - Временная метка.
    Поле details - Описание, что изменилось.
    """
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='audit_logs'
    )
    action = models.CharField(
        'Действие',
        max_length=MAX_ACTION_LENGTH,
        choices=ACTION_CHOICES
    )
    target = models.CharField('Объект', max_length=MAX_RESOURCE_LENGTH)
    timestamp = models.DateTimeField('Временная метка', auto_now_add=True)
    details = models.TextField('Детали', null=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Журнал действий'
        verbose_name_plural = 'Журналы действий'

    def __str__(self):
        return f"{self.user} {self.action} {self.target} at {self.timestamp}"


class Category(models.Model):
    """
    Модель Category для присвоения категорий ресурсам.
    """
    name = models.CharField(
        'Название',
        max_length=MAX_RESOURCE_LENGTH,
        unique=True
    )
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Password(models.Model):
    """
    Модель Password для хранения паролей ресурсов.
    """
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='user_passwords'
    )
    resource = models.CharField('Ресурс', max_length=MAX_RESOURCE_LENGTH)
    resource_icon = models.ImageField(
        upload_to='resource_icons/',
        null=True,
        blank=True,
        verbose_name='Иконка ресурса'
    )
    login = models.CharField(
        'Логин на ресурсе',
        max_length=MAX_RESOURCE_LENGTH
    )
    password = encrypt(models.CharField(
        'Пароль',
        max_length=MAX_RESOURCE_LENGTH)
    )
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='passwords'
    )

    class Meta:
        ordering = ('resource', )
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'

    def __str__(self):
        return self.resource

    def get_absolute_url(self):
        return reverse(
            'passwords:password_detail',
            kwargs={'password_id': self.pk}
        )
