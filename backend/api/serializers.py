from rest_framework import serializers

from passwords.models import Password


class PasswordSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Password
        fields = ['user', 'resource', 'login', 'password']


class PasswordListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Password
        fields = ['resource']
