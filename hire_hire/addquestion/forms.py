from django import forms

from interview.models import Language
from .models import AddQuestion


class AddQuestionForm(forms.ModelForm):
    """Add question form."""

    class Meta:
        model = AddQuestion
        fields = ('language', 'text', 'answer', )
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
            'language': forms.Select(attrs={'class': 'form-control'}),
        }
        initial = {
            'language': Language.objects.get(title='Python'),
        }
