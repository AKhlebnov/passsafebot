from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from passwords.views import IndexView


handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('users.urls')),
    path('passwords/', include('passwords.urls')),
    path('', IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
