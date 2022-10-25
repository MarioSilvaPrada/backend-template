from django.urls import path
# from rest_framework import routers

from enode import views

# router = routers.SimpleRouter()
# router.register(r'^vehicle/<vehicle_id>/(?P<field>\w+)/$', views.get_vehicle_id, basename='enode-vehicle')

urlpatterns = [
    path('token/', views.enode_token_view),
    path('link/', views.enode_link_view),
    path('me/', views.get_enode_user),
    path('vehicle/', views.get_vehicle),
    path('vehicle/<str:vehicle_id>/', views.get_vehicle_id),
    path('vehicle/<str:vehicle_id>/<str:field>/', views.get_vehicle_id),
    path('vehicle/<str:vehicle_id>/charge', views.control_charging),
    path('charger/', views.get_charger),
    path('schedules/', views.get_schedules),
    path('health/', views.get_car_health),
    path('available-vendors/', views.get_available_vendors),
]
