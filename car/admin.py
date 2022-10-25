from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['vendor', 'user']
    search_fields = ['user__email']
    # list_filter = ('is_sold',)
