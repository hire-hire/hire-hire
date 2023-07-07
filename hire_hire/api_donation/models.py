from django.db import models
from django.conf import settings


class Currency(models.Model):
    """
    Модель валют. Нужен только айдишник и строка, чойс из констант
    Константы взять в юкассы
    """
    name = models.CharField(
        'наименование',
        max_length=10,
        choices=settings.DONATION_SETTINGS.get('currencies'),
    )

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'

    def __str__(self):
        return self.name


class Price(models.Model):
    """
    Модель платежей
    Нужен айдишник, инт цены, связь с валютой
    """

    value = models.IntegerField('значение')

    currency = models.ForeignKey(
        Currency,
        verbose_name='валюта',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'

    def __str__(self):
        return str(self.value)


class IdempotenceKey(models.Model):
    """
    Моделька для уникальный ключей платежей
    Нужен айдишник, строка-ключ с признаком уникальности
    """

    value = models.UUIDField('значение', unique=True)

    creation_date = models.DateField(
        'дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'ключ идемпотенции'
        verbose_name_plural = 'ключи идемпотенции'
