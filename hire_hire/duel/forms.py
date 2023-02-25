from django import forms
from django.conf import settings


class DuelSettingsForm(forms.Form):
    questions_count = forms.TypedChoiceField(
        coerce=int,
        choices=settings.QUESTION_COUNT_CHOICE,
        widget=forms.Select(
            attrs={'class': 'test-settings-form__select '
                            'duel-settings__select page__text'},
        ),
    )
    first_player = forms.CharField(
        max_length=100,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'class': 'duel-settings__input page__text',
                'placeholder': 'Игрок 1',
            },
        ),
    )
    second_player = forms.CharField(
        max_length=100,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'class': 'duel-settings__input page__text',
                'placeholder': 'Игрок 2',
            },
        ),
    )
