from django.contrib.auth import get_user_model
from django.db import models

from duel.managers import DuelManager, DuelPlayerManager, DuelQuestionManager
from interview.models import Question

User = get_user_model()


class Duel(models.Model):
    """
    Объект дуэли.
    В MVP:
        - может содержать овнера
        - считает неверные ответы
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='duel',
        verbose_name='владец игры',
    )

    wrong_answers_count = models.IntegerField(
        'количество неправильных ответов',
        default=0,
    )

    objects = DuelManager()

    class Meta:
        verbose_name = 'дуэль'
        verbose_name_plural = 'дуэли'

    def __str__(self):
        return f'дуэль {self.pk}'


class DuelPlayer(models.Model):
    """
    Объект счетчика в дуэли.
    В MVP:
        - хранит имя игрока
        - хранит текущий счет
        - связана с дуэлью
    """

    name = models.CharField(
        'имя игрока',
        max_length=100,
        default='Игрок',
    )

    good_answers_count = models.IntegerField(
        default=0,
        verbose_name='счетчик',
    )

    duel = models.ForeignKey(
        Duel,
        on_delete=models.CASCADE,
        related_name='players',
        verbose_name='дуэль',
    )
    objects = DuelPlayerManager()

    class Meta:
        verbose_name = 'участник дуэли'
        verbose_name_plural = 'участники дуэли'
        ordering = ['pk',]

    def __str__(self):
        return self.name[:15]


class DuelQuestion(models.Model):
    """
    Объект вопроса в рамках дуэли.
    В MVP:
        - хранит вопрос для конкретной дуэли
        - хранит статус вопроса
    """

    duel = models.ForeignKey(
        Duel,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='дуэль',
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='duel',
        verbose_name='вопрос',
    )

    is_answered = models.BooleanField(
        'дан ответ',
    )

    objects = DuelQuestionManager()

    class Meta:
        verbose_name = 'вопрос в дуэли'
        verbose_name_plural = 'вопросы в дуэли'

    def __str__(self):
        return f'вопрос дуэли {self.pk}'
