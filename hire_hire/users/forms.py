from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
