from django.contrib.auth import get_user_model
from django.db import models

from add_question.managers import AddQuestionManager
from interview.models import AbstractQuestion, Language

User = get_user_model()


class AddQuestion(AbstractQuestion):
    """
    Наследуется от AbstractQuestion.
    Предложенный вопрос.
    + автор?
    """
    STATUS_CHOICES = (
        ('proposed', 'Предложенный'),
        ('rejected', 'Отклоненный'),
        ('approved', 'Одобренный'),
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='add_questions',
        verbose_name='язык',
        default=1,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='add_questions',
        verbose_name='автор',
    )
    ip_address = models.GenericIPAddressField(
        'IP-адрес',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='proposed',
        verbose_name='статус',
    )

    objects = AddQuestionManager()

    class Meta:
        verbose_name = 'предложенный вопрос'
        verbose_name_plural = 'предложенные вопросы'
