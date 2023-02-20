from django.db import models


class TeamRole(models.Model):
    name = models.CharField(
        'название',
        max_length=150,
    )

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __str__(self):
        return self.name
