from django.contrib.auth import get_user_model
from django.db import models

from add_question.managers import AddQuestionManager
from interview.models import AbstractQuestion, Language

User = get_user_model()


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

    user_cookie_id = models.CharField(
        'user cookie id',
        max_length=32,
        blank=True,
        null=True,
    )

    objects = AddQuestionManager()

    class Meta:
        verbose_name = 'предложенный вопрос'
        verbose_name_plural = 'предложенные вопросы'
