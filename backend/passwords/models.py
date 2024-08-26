from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Password(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_passwords'
    )
    resource = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('resource', )
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'

    def __str__(self):
        return self.resource
