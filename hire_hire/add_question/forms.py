from django import forms

from add_question.models import AddQuestion


class AddQuestionForm(forms.ModelForm):

    class Meta:
        model = AddQuestion
        fields = ('text', 'answer')
        labels = {
            'text': 'Ваш вопрос',
            'answer': 'Ваш ответ',
        }

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
        }

    def clean(self):
        add_questions_for24_count = self.initial.get(
            'add_questions_for24_count')
        limit_add_questions_per_day = self.initial.get(
            'limit_add_questions_per_day')
        if add_questions_for24_count >= limit_add_questions_per_day:
            self.add_error(None, 'Вы исчерпали лимит вопросов на день.')
        return self.cleaned_data
