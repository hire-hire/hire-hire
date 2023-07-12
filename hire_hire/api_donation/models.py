from django.conf import settings
from django.db import models


class Currency(models.Model):

    name = models.CharField(
        'наименование',
        max_length=10,
        choices=settings.DONATION.currencies,
    )

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'

    def __str__(self):
        return self.name


class Price(models.Model):

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
        return str(self.value) + ' ' + str(self.currency.name)


class IdempotenceKey(models.Model):

    value = models.UUIDField('значение', unique=True)

    creation_date = models.DateField(
        'дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'ключ идемпотенции'
        verbose_name_plural = 'ключи идемпотенции'

    def __str__(self):
        return str(self.value)
