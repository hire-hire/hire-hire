from django.db import models


class DeveloperData(models.Model):
    """Информация о разработчиках проекта."""

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    photo = models.ImageField(
        'фото разработчика',
        blank=False,
        help_text='Добавьте фото',
    )
    web_site = models.URLField(
        'сайт-портфолио',
        max_length=200,
        blank=True,
        null=True,
        help_text='Укажите сайт разработчика',
    )
    bio = models.TextField(
        'о себе',
        blank=True,
        null=True,
        help_text='Расскажите кратко о себе',
    )

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class FAQ(models.Model):
    pass
