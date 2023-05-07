from django.db import models
from django.core.exceptions import ValidationError


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

    def save(self, *args, **kwargs):
        """Создавать более трех контактов запрещено, нарушает верстку."""
        if ContributorContact.objects.select_related().count() >= 3:
            return ValidationError('Можно добавить не более трех контактов')

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return f'{self.social_network}: {self.contact}'
