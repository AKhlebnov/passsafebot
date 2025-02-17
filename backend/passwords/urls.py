from django.urls import path

from .views import IndexView, PasswordListView

app_name = 'passwords'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('passwords/', PasswordListView.as_view(), name='password_list'),
]
