from django.contrib import admin
from .models import EnodeTokenModel


@admin.register(EnodeTokenModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['access_token', 'expires_date']
