from django.urls import path
from data import views

urlpatterns = [
    path('energy/', views.get_energy_prices),
]
