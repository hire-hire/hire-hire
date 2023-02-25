from django import forms


class InterviewSettingsForm(forms.Form):
    QUESTION_COUNT_CHOICE = (
        (10, '10 вопросов'),
        (20, '20 вопросов'),
        (30, '30 вопросов'),
    )
    questions_count = forms.TypedChoiceField(
        coerce=int,
        choices=QUESTION_COUNT_CHOICE,
        label='Количество вопросов',
        widget=forms.Select(
            attrs={'class': 'test-settings-form__select page__text'},
        ),
    )
