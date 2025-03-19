from django.contrib import admin

from .models import AuditLog, Category, Password


admin.site.register(AuditLog)
admin.site.register(Category)
admin.site.register(Password)
