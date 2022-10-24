from rest_framework import generics
from .serializers import UserSerializer
from .models import User


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
    