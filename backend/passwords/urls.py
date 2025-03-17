from django.urls import path

from .views import (
    PasswordListView, PasswordCreateView,
    PasswordDetailView, PasswordUpdateView, PasswordDeleteView,
    UserDetailView, UserEditUpdateView,
)

app_name = 'passwords'

urlpatterns = [
    path('', PasswordListView.as_view(), name='password_list'),
    path(
        'create/',
        PasswordCreateView.as_view(), name='password_create'
    ),
    path(
        '<int:password_id>/',
        PasswordDetailView.as_view(), name='password_detail'
    ),
    path(
        '<int:password_id>/edit/',
        PasswordUpdateView.as_view(), name='password_edit'
    ),
    path(
        '<int:password_id>/delete/',
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
