from rest_framework import viewsets

from passwords.models import Password
from .serializers import PasswordSerializer


class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
