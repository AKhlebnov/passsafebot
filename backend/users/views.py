from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView

from core.mixins import UserMixin, OwnerRequiredMixin

User = get_user_model()


class UserDetailView(
    UserMixin, OwnerRequiredMixin,
    LoginRequiredMixin, DetailView
):
    """Класс для страницы пользователя"""

    template_name = 'passwords/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class UserEditUpdateView(
    UserMixin, OwnerRequiredMixin,
    LoginRequiredMixin, UpdateView
):
    """Класс для редактирования страницы пользователя"""

    fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
    template_name = 'passwords/user.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
