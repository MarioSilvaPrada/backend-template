from django.urls import path
from enode import views


urlpatterns = [
    path('token/', views.enode_token_view),
    path('link/', views.enode_link_view),
    path('me/', views.get_enode_user),
]
