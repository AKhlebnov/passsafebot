from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()


class OwnerRequiredMixin:
    """Миксин для проверки владельца объекта"""

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != request.user:  # Проверяем владельца объекта
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class UserMixin:
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
