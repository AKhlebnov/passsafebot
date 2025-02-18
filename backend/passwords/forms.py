from django import forms
from .models import Password


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['resource', 'resource_icon', 'login', 'password', 'category']
        widgets = {
            # Показывать звёздочки при ошибке
            'password': forms.PasswordInput(render_value=True)
        }
