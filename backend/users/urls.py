from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .views import UserDetailView, UserEditUpdateView

app_name = 'users'

urlpatterns = [
    # Аутентификация
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Смена пароля
    path(
        'auth/password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done')
        ),
        name='password_change'
    ),
    path(
        'auth/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ),
        name='password_change_done'
    ),

    # Восстановление пароля
    path(
        'auth/password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
            success_url=reverse_lazy('users:password_reset_done'),
        ),
        name='password_reset'
    ),
    path(
        'auth/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done'
    ),
    path(
        'auth/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),
    path(
        'auth/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete'
    ),

    # Профиль
    path(
        'profile/<slug:username>/',
        UserDetailView.as_view(),
        name='profile'
    ),
    path(
        'profile/<slug:username>/edit/',
        UserEditUpdateView.as_view(),
        name='edit_profile'
    ),

    # Регистрация
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('index'),
        ),
        name='registration',
    ),
]
