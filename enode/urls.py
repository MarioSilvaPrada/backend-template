from django.urls import path
from enode import views

urlpatterns = [
    path('token/', views.enode_token_view),
    path('link/', views.enode_link_view),
    path('me/', views.get_enode_user),
    path('vehicle/', views.get_vehicle),
    path('vehicle/<str:vehicle_id>/', views.get_vehicle_id),
    path('vehicle/<str:vehicle_id>/<str:field>/', views.get_vehicle_id),
    path('vehicle/<str:vehicle_id>/charge', views.control_charging),
    path('charge/actions/<str:action_id>', views.get_charger_action),
    path('charge/', views.get_charger),
    path('schedules/', views.get_schedules),
    path('health/', views.get_car_health),
    path('available-vendors/', views.get_available_vendors),
    path('webhook/', views.webhook),
    path('statistics/charging/', views.schedule_statistics),
]
