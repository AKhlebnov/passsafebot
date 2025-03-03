from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import PasswordForm
from .models import Password

User = get_user_model()


class UserMixin:
    model = User
    slug_url_kwarg = 'username'


class IndexView(TemplateView):
    template_name = "passwords/index.html"


class PasswordListView(LoginRequiredMixin, ListView):
    model = Password
    template_name = 'passwords/password_list.html'
    context_object_name = 'passwords'
    paginate_by = 10

    def get_queryset(self):
        return Password.objects.filter(
            user=self.request.user
        ).order_by('-updated_at')


class PasswordCreateView(LoginRequiredMixin, CreateView):
    model = Password
    form_class = PasswordForm
    template_name = 'passwords/password_form.html'
    success_url = reverse_lazy('passwords:password_list')

    def form_valid(self, form):
        # Привязываем ресурс к текущему пользователю
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordDetailView(LoginRequiredMixin, DetailView):
    model = Password
    pk_url_kwarg = 'password_id'
    template_name = 'passwords/password_detail.html'

    def dispatch(self, request, *args, **kwargs):
        password = self.get_object()

        if request.user == password.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class PasswordUpdateView(LoginRequiredMixin, UpdateView):
    model = Password
    form_class = PasswordForm
    template_name = 'passwords/password_form.html'
    pk_url_kwarg = 'password_id'

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # Возвращаем URL для детальной страницы ресурса
        return reverse_lazy('passwords:password_detail', kwargs={'password_id': self.object.pk})


class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    model = Password
    template_name = 'passwords/password_delete.html'
    pk_url_kwarg = 'password_id'
    success_url = reverse_lazy('passwords:password_list')

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        context['password'] = instance
        return context


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
        print(context)
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
            'passwords:profile',
            kwargs={'username': self.request.user.username}
        )
