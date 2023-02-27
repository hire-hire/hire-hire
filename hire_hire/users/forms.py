from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form__input page__text'
