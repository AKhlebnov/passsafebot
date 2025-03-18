from django.http import Http404
from django.contrib.auth import get_user_model

from passwords.models import Password

User = get_user_model()


class OwnerRequiredMixin:
    """Миксин для проверки владельца объекта"""

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()

        if isinstance(instance, User):
            # Проверяем напрямую для пользователя
            if instance != request.user:
                raise Http404()
        elif isinstance(instance, Password):
            # Проверяем через поле user для пароля
            if instance.user != request.user:
                raise Http404()
        else:
            raise Http404()

        return super().dispatch(request, *args, **kwargs)


class UserMixin:
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'


class BasePasswordMixin:
    """Базовый миксин для работы с моделью Password"""
    model = Password
    pk_url_kwarg = 'password_id'
