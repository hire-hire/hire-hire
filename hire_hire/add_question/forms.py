from django import forms
# from django.conf import settings

from add_question.models import AddQuestion
# from interview.models import Language


# limit_add_questions_per_day = getattr(
#         settings, 'LIMIT_ADD_QUESTIONS_PER_DAY', 10)


class AddQuestionForm(forms.ModelForm):

    class Meta:
        model = AddQuestion
        fields = ('language', 'text', 'answer')
        labels = {'language': 'Язык',
                  'text': 'Ваш вопрос',
                  'answer': 'Ваш ответ', }

        widgets = {
            'text': forms.Textarea(attrs={
                'id': 'question',
                'class': 'offer__textarea page__text',
                'minlength': '10',
                'maxlength': '500',
                'placeholder': 'Введите вопрос',
                'required': True,
            }),
            'answer': forms.Textarea(attrs={
                'id': 'answer',
                'class': 'offer__textarea page__text',
                'minlength': '10',
                'maxlength': '500',
                'placeholder': 'Введите ответ',
                'required': True,
            }),
            # 'language': forms.Select(attrs={'class': 'form-control'}),
        }
        # initial = {
        #     'language': Language.objects.get(title='Python'),
        # }

    def clean(self):
        cleaned_data = super().clean()
        add_questions_for24_count = self.initial.get(
            'add_questions_for24_count')
        limit_add_questions_per_day = self.initial.get(
            'limit_add_questions_per_day')
        if add_questions_for24_count >= limit_add_questions_per_day:
            self.add_error(None, 'Вы исчерпали лимит вопросов на день.')
            # raise forms.ValidationError('Вы исчерпали лимит вопросов на день.')
        return cleaned_data
