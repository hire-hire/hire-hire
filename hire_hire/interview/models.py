from django.contrib.auth import get_user_model
from django.db import models

from interview.managers import InterviewManager, QuestionManager

User = get_user_model()


class Category(models.Model):
    """
    Сущность-раздел для агрегации "языков" и вопросов.
    """

    title = models.CharField('название', max_length=40)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Language(models.Model):
    """
    Язык программирования - одна из сущностей,
    объединяющих и разделяющих вопросы.
    Выше категория.
    """

    title = models.CharField('название', max_length=40)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='languages',
        verbose_name='категория',
        null=True,
    )

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'

    def __str__(self):
        return self.title


class AbstractQuestion(models.Model):
    """
    Модель для наследования.
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
        abstract = True
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:45]


class Question(AbstractQuestion):
    """
    Наследуется от AbstractQuestion.
    """
    pass


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
        related_name='interviews',
        verbose_name='пользователь',
    )

    questions = models.ManyToManyField(Question, verbose_name='набор вопросов')

    objects = InterviewManager()

    class Meta:
        verbose_name = 'интервью'
        verbose_name_plural = 'интервью'

    def __str__(self):
        return f'интервью {self.pk}'
