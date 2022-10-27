from django.contrib import admin
from .models import EnergyPrice
# Register your models here.


@admin.register(EnergyPrice)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['date']
