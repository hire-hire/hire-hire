from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from interview.managers import (
    InterviewManager,
    QuestionLastDateUsedManage,
    QuestionManager,
)

User = get_user_model()


class Entity(models.Model):
    title = models.CharField('название', max_length=40)

    icon = models.ImageField(
        'иконка',
        upload_to='icons',
        help_text='иконка',
        default='icons/python3_logo.jpg',
    )

    class Meta:
        abstract = True


class Category(Entity):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Language(Entity):
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
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='язык',
    )

    text = models.TextField(
        'текст вопроса',
        max_length=500,
        validators=[MinLengthValidator(10)],
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='questions',
        verbose_name='автор',
    )

    objects = QuestionManager()

    class Meta:
        abstract = True
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:45]


class Question(AbstractQuestion):
    pass


class QuestionAnswer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='вопрос',
    )

    text = models.TextField(
        'ответ',
        max_length=500,
        validators=[MinLengthValidator(2)],
    )

    is_correct = models.BooleanField(
        'правильный ответ',
    )

    class Meta:
        verbose_name = 'ответ на вопрос'
        verbose_name_plural = 'ответы на вопрос'

    def __str__(self):
        return f'{self.text[:45]}'


class QuestionLastDateUsed(models.Model):
    user = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        related_name='questions_last_date_used',
        verbose_name='пользователь',
    )
    question = models.ForeignKey(
        Question,
        db_index=True,
        on_delete=models.CASCADE,
        related_name='questions_last_date_used',
        verbose_name='вопрос',
    )
    date = models.DateTimeField(
        'дата использования',
        auto_now=True,
    )

    objects = QuestionLastDateUsedManage()

    class Meta:
        verbose_name = 'дата последнего использования вопроса'
        verbose_name_plural = 'даты последних использований вопросов'

        unique_together = ('user', 'question')

    def __str__(self):
        return f'{self.user.pk} - {self.question.pk} - {self.time}'


class LastUserRefreshDate(models.Model):
    user = models.OneToOneField(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        related_name='questions_refresh_date',
        verbose_name='обновление лимита',
    )
    date = models.DateTimeField(
        'дата обновления',
        auto_now=True,
    )


class Interview(models.Model):
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
