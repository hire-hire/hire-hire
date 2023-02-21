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
        if len(ids) < cnt:
            cnt = len(ids)
        rand_ids = sample(ids, cnt)
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

    text = models.CharField('текст вопроса', max_length=256)

    answer = models.TextField('правильный ответ', max_length=256)

    objects = QuestionManager()

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:15]


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
