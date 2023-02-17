from django.contrib.auth import get_user_model
from django.db import models

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

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Interview(models.Model):
    """
    Объект конкретного интервью.
    В MVP:
        - содержит набор вопросов
        - в первом приближении не связан с пользователем
        - во втором приближении может быть связан с пользователем
        - в первом приближении содержит просто int-счетчик для вопросов.
        дальше это можно переделать в промежуточную модель с вопросами,
        где так же можно хранить данные ответы.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='interviews',
        verbose_name='пользователь'
    )

    questions_asked = models.IntegerField('вопросов задано', default=0)

    questions = models.ManyToManyField(
        Question,
        verbose_name='набор вопросов'
    )

    class Meta:
        verbose_name = 'интервью'
        verbose_name_plural = 'интервью'
