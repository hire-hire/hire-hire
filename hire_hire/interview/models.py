from random import sample

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class QuestionManager(models.Manager):
    """
    Кастомный менеджер для добавления метода
    выборки данного кол-ва случайных вопросов.
    """

    def random(self, cnt):
        ids = list(self.get_queryset().values_list('id', flat=True))
        rand_ids = sample(ids, min(cnt, len(ids)))
        return self.get_queryset().filter(id__in=rand_ids)


class Language(models.Model):
    """
    Язык программирования - одна из сущностей,
    объединяющих и разделяющих вопросы.
    Выше специализация, ниже - сложность.
    В MVP пока без них.
    """

    title = models.CharField('название', max_length=40)

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Вопрос. В MVP:
        - содержит верный ответ
        - связан только с Языком Программирования.
    """

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='вопрос',
    )

    text = models.TextField('текст вопроса')

    answer = models.TextField('правильный ответ')

    objects = QuestionManager()

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:45]


class Interview(models.Model):
    """
    Объект конкретного интервью.
    В MVP:
        - содержит набор вопросов
        - может быть связан с пользователем
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='interviews',
        verbose_name='пользователь',
    )

    questions = models.ManyToManyField(Question, verbose_name='набор вопросов')

    class Meta:
        verbose_name = 'интервью'
        verbose_name_plural = 'интервью'


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
        related_name='duels',
        null=True,
    )

    wrong_answers = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'дуэль'
        verbose_name_plural = 'дуэли'


class DuelPlayer(models.Model):
    """
    Объект счетчика в дуэли.
    В MVP:
        - хранит имя игрока
        - хранит текущий счет
        - связана с дуэлью
    """

    name = models.CharField(
        max_length=100,
        default='Игрок',
        verbose_name='имя игрока'
    )

    counter = models.IntegerField(default=0, verbose_name='счетчик')

    duel = models.ForeignKey(
        Duel,
        on_delete=models.CASCADE,
        related_name='players',
    )

    class Meta:
        verbose_name = 'участник дуэли'
        verbose_name_plural = 'участники дуэли'

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
        verbose_name='дуэль'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='duels',
        verbose_name='вопрос'
    )

    is_answered = models.BooleanField('дан ответ')

    class Meta:
        verbose_name = 'вопрос в дуэли'
        verbose_name_plural = 'вопросы в дуэли'
