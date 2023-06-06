from django.conf import settings
from django.db import models

from contributors.managers import ContributorContactManager


class ContributorContact(models.Model):
    contributor = models.ForeignKey(
        'contributors.Contributor',
        verbose_name='член команды',
        on_delete=models.CASCADE,
        related_name='contacts',
    )
    social_network = models.CharField(
        'название соцсети',
        max_length=150,
    )
    contact = models.URLField(
        'контакт',
        blank=True,
        null=True,
        help_text='Укажите ссылку (github, telegram, vk и другие)',
    )
    objects = ContributorContactManager()

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return f'{self.social_network}: {self.contact}'

    def save(self, *args, **kwargs):
        if not self.pk and (
            ContributorContact.objects.
            get_contributor_contacts_count(self.contributor) >=
            settings.LIMIT_CONTRIBUTORS_CONTACTS
        ):
            raise ValueError('Нельзя добавлять больше 3х контактов')

        super().save(*args, **kwargs)
