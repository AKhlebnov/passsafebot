from rest_framework import permissions, viewsets

from passwords.models import Password
from .serializers import PasswordSerializer, PasswordListSerializer


class PasswordViewSet(viewsets.ModelViewSet):
    """
    Класс представления для обработки модели Password.
    """
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer

    def get_queryset(self):
        """
        Метод возвращает пароли текущего пользователя.
        """
        return super().get_queryset().filter(user=self.request.user)

    def get_serializer_class(self):
        """
        Метод возвращает соответствующий класс сериализатора
        в зависимости от действия.
        """
        # Для действия 'list' используем специальный сериализатор
        if self.action == 'list':
            return PasswordListSerializer
        # Для всех остальных действий используем дефолтный
        return PasswordSerializer
