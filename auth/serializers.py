from user.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')

class RegisterWithPhoneSerializer(serializers.Serializer):

    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    phone = serializers.RegexField("^\+[1-9]{1}[0-9]{3,14}$")

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError('A user with this phone number already exists!')
        return value

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'phone': self.validated_data.get('phone', ''),
        }

    def custom_signup(self, request, user):
        pass

    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.save()
        print('O meu user',user)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
    