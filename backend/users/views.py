from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

User = get_user_model()


class UserMixin:
    model = User
    slug_url_kwarg = 'username'


class UserDetailView(UserMixin, LoginRequiredMixin, DetailView):
    """Класс для страницы пользователя"""

    template_name = 'passwords/profile.html'
    slug_field = 'username'
    context_object_name = 'profile'

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()

        if request.user == user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class UserEditUpdateView(UserMixin, LoginRequiredMixin, UpdateView):
    """Класс для редактирования страницы пользователя"""

    fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
    template_name = 'passwords/user.html'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        return get_object_or_404(User.objects.filter(username=username))

    def get_success_url(self):
        return reverse_lazy(
            'users:profile',
            kwargs={'username': self.object.username}
        )
