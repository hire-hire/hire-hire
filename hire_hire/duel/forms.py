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


class DuelFlowAnsweredForm(forms.Form):
    player_pk = forms.TypedChoiceField(
        coerce=int,
        widget=forms.RadioSelect(
            attrs={
                'class': 'duel__radio '
            },
        ),
    )

    def __init__(self, players, can_choose_winner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player_pk'].choices = players

        if not can_choose_winner:
            self.fields['player_pk'].widget.attrs['disabled'] = True
