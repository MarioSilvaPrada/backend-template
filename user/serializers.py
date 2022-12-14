from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
        # read_only_fields = ('id', 'user_permissions', 'groups', 'password')
