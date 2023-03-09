from django import forms

from .models import AddQuestion


class AddQuestionForm(forms.ModelForm):
    """Add question form."""

    class Meta:
        model = AddQuestion
        fields = ('language', 'text', 'answer', )
        labels = {'language': 'Язык',
                  'text': 'Предложите вопрос',
                  'answer': 'Ваш ответ', }