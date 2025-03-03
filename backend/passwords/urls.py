from django.urls import path

from .views import (
    IndexView, PasswordListView, PasswordCreateView,
    PasswordDetailView, PasswordUpdateView, PasswordDeleteView,
    UserDetailView, UserEditUpdateView,
)

app_name = 'passwords'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('passwords/', PasswordListView.as_view(), name='password_list'),
    path(
        'passwords/create/',
        PasswordCreateView.as_view(), name='password_create'
    ),
    path(
        'passwords/<int:password_id>/',
        PasswordDetailView.as_view(), name='password_detail'
    ),
    path(
        'passwords/<int:password_id>/edit/',
        PasswordUpdateView.as_view(), name='password_edit'
    ),
    path(
        'passwords/<int:password_id>/delete/',
        PasswordDeleteView.as_view(), name='password_delete'
    ),
    path(
        'profile/<slug:username>/',
        UserDetailView.as_view(),
        name='profile'
    ),
    path(
        'profile/<slug:username>/edit/',
        UserEditUpdateView.as_view(),
        name='edit_profile'
    )
]
