from django.views.generic import TemplateView


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
