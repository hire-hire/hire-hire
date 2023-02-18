from django.db import models
from sorl.thumbnail import ImageField


class OurTeam(models.Model):
    class Role(models.IntegerChoices):
        GURU = 0, 'гуру проекта'
        PM = 1, 'менеджеры проекта'
        FRONT_END = 2, 'фронтенд разработчики'
        BACK_END = 3, 'бэкенд-разработчики'
        QA = 4, 'QA-тестировщики'
        UI_UX_DESIGNER = 5, 'UX/UI-дизайнеры'

    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=False,
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
        blank=False,
    )
    middle_name = models.CharField(
        'отчество',
        max_length=150,
        blank=True,
        null=True,
    )
    photo = ImageField(
        'фото',
        blank=False,
        upload_to='team',
        help_text='Добавьте фото',
    )
    role = models.PositiveSmallIntegerField(
        'роль в команде',
        choices=Role.choices,
    )
    contact = models.URLField(
        'контакт',
        blank=True,
        null=True,
        help_text='Укажите ссылку (github, telegram, vk и другие)',
    )

    class Meta:
        verbose_name = 'информация о команде'
        verbose_name_plural = 'информация о команде'
        ordering = ('role',)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
