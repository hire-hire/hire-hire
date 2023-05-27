from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer


User = get_user_model()


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            User.id.field.name,
            User.username.field.name,
            User.is_duel_moderator.field.name,
        )
