from django.urls import path
from car import views


urlpatterns = [
    path('enode-token/', views.enode_token_view),
]
