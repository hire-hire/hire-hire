from django import forms
from django.conf import settings


class InterviewSettingsForm(forms.Form):
    questions_count = forms.TypedChoiceField(
        coerce=int,
        choices=settings.QUESTION_COUNT_CHOICE,
        widget=forms.Select(
            attrs={'class': 'test-settings-form__select page__text'},
        ),
    )
