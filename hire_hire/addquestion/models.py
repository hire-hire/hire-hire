from django.contrib.auth import get_user_model
from django.db import models

from interview.models import AbstractQuestion, Language

User = get_user_model()


class AddQuestion(AbstractQuestion):
    """
    Наследуется от AbstractQuestion.
    Предложенный вопрос.
    + автор?
    """
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='addquestions',
        verbose_name='язык',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='addquestions',
        verbose_name='автор',
    )
    ip_address = models.CharField(
        'IP-адрес',
        max_length=50,
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        blank=True,
        null=True,
    )
