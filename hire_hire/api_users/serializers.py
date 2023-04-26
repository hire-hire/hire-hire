from django.conf import settings
from django.core.exceptions import ValidationError
from djoser.serializers import UserCreateSerializer


class NewUserSerializer(UserCreateSerializer):

    def validate(self, attrs):
        password = attrs.get('password''')
        if len(password) > settings.PASSWORD_MAX_LENGTH:
            raise ValidationError('From 8 to 40 characters.')

        return super().validate(attrs)
