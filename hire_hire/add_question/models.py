# from django.conf import settings
from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
from django.db import models

from add_question.managers import AddQuestionManager
from interview.models import AbstractQuestion, Language

User = get_user_model()


# from rest_framework import serializers


class AddQuestion(AbstractQuestion):

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        default=1,
        related_name='add_questions',
        verbose_name='язык',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='add_questions',
        verbose_name='автор',
    )
    ip_address = models.GenericIPAddressField(
        'IP-адрес',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
    )

    class StatusChoice(models.TextChoices):
        PROPOSED = 'proposed', 'Предложенный'
        REJECTED = 'rejected', 'Отклоненный'
        APPROVED = 'approved', 'Одобренный'

    status = models.CharField(
        'статус',
        max_length=10,
        choices=StatusChoice.choices,
        default=StatusChoice.PROPOSED,
    )

    user_cookie = models.CharField(
        'user cookie id',
        max_length=32,
        blank=True,
        null=True,
    )

    objects = AddQuestionManager()

    class Meta:
        verbose_name = 'предложенный вопрос'
        verbose_name_plural = 'предложенные вопросы'

    # def save(self, *args, **kwargs):
    #     # raise ValidationError('save ValidationError')
    #     # print('save!!!!!!!!!!!!!!!!!!!!!!!!')
    #     # print(self.author)
    #     # print(self.user_cookie)
    #     if AddQuestion.objects.get_24_hours_added_question(
    #         author=self.author,
    #         user_cookie=self.user_cookie,
    #     ) >= settings.LIMIT_ADD_QUESTIONS_PER_DAY:
    #         raise serializers.ValidationError('Вы исчерпали лимит вопросов на день.')
    #     super().save(*args, **kwargs)

    # def clean(self):
    #     raise ValidationError('clean ValidationError')
