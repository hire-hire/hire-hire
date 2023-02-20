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
    role = models.ForeignKey(
        'static_info.TeamRole',
        verbose_name='роль в команде',
        on_delete=models.PROTECT,
    )
    contact = models.URLField(
        'контакт',
        blank=True,
        null=True,
        help_text='Укажите ссылку (github, telegram, vk и другие)',
    )

    class Meta:
        verbose_name = 'член команды'
        verbose_name_plural = 'члены команды'
        ordering = ('role',)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
