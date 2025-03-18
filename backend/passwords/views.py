from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
)

from core.mixins import BasePasswordMixin, OwnerRequiredMixin
from .forms import PasswordForm
from .models import Password

User = get_user_model()


class IndexView(TemplateView):
    """
    Главная страница приложения.
    """
    template_name = "passwords/index.html"


class PasswordListView(LoginRequiredMixin, ListView):
    """
    Список всех паролей.
    Выводит список всех паролей текущего пользователя.
    """
    model = Password
    template_name = 'passwords/password_list.html'
    context_object_name = 'passwords'
    paginate_by = 10

    def get_queryset(self):
        return Password.objects.filter(
            user=self.request.user
        ).order_by('-updated_at')


class PasswordCreateView(LoginRequiredMixin, CreateView):
    """
    Создание нового пароля.

    Доступно только авторизованным пользователям.
    После успешного создания перенаправляет на список паролей.
    """
    model = Password
    form_class = PasswordForm
    template_name = 'passwords/password_form.html'
    success_url = reverse_lazy('passwords:password_list')

    def form_valid(self, form):
        # Привязываем ресурс к текущему пользователю
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordDetailView(
    LoginRequiredMixin, OwnerRequiredMixin,
    BasePasswordMixin, DetailView
):
    """
    Детальная информация о пароле.
    Доступна только владельцу пароля.
    """
    template_name = 'passwords/password_detail.html'


class PasswordUpdateView(
    LoginRequiredMixin, OwnerRequiredMixin,
    BasePasswordMixin, UpdateView
):
    """
    Редактирование пароля.
    Доступна только владельцу пароля.
    """
    form_class = PasswordForm
    template_name = 'passwords/password_form.html'

    def get_success_url(self):
        # Возвращаем URL для детальной страницы ресурса
        return self.object.get_absolute_url()


class PasswordDeleteView(
    LoginRequiredMixin, OwnerRequiredMixin,
    BasePasswordMixin, DeleteView
):
    """
    Удаление пароля.
    Доступна только владельцу пароля.
    """
    template_name = 'passwords/password_delete.html'
    success_url = reverse_lazy('passwords:password_list')
