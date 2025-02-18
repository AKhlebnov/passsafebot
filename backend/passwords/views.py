from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PasswordForm
from .models import Password


class IndexView(TemplateView):
    template_name = "passwords/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаём мок-данные в шаблон
        context['resources'] = [
            {'name': 'GitHub', 'category': 'Development'},
            {'name': 'Google', 'category': 'Search'},
        ]
        return context


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
