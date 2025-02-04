from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@mail.com'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()

        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже зарегистрирован")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = 'Только буквы, цифры и @/./+/-/_'
