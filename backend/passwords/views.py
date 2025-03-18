from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
)

from .forms import PasswordForm
from .models import Password

User = get_user_model()


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
        return reverse_lazy(
            'passwords:password_detail',
            kwargs={'password_id': self.object.pk}
        )


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
