from django.db import models


class Question(models.Model):
    '''Модель вопросов и ответов для интервью'''
    text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.text
