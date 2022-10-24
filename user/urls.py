
from django.urls import path, re_path
from .views import ManageUserView
from dj_rest_auth.views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('me/', ManageUserView.as_view()),
]
