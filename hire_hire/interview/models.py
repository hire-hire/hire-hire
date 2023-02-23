from django.contrib.auth import get_user_model
from django.db import models

from interview.managers import QuestionManager, DuelQuestionManager, DuelPlayer

User = get_user_model()


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

    def __str__(self):
        return f'интервью {self.pk}'


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
        null=True,
        related_name='duels',
        verbose_name='владец игры',
    )

    wrong_answers_count = models.IntegerField(
        'количество неправильных ответов',
        default=0,
    )

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
    objects = DuelPlayer()

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
        verbose_name='дуэль',
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='duels',
        verbose_name='вопрос',
    )

    is_answered = models.BooleanField('дан ответ')

    objects = DuelQuestionManager()

    class Meta:
        verbose_name = 'вопрос в дуэли'
        verbose_name_plural = 'вопросы в дуэли'

    def __str__(self):
        return f'вопрос дуэли {self.pk}'
