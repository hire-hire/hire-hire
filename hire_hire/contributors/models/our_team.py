from django.db import models
from sorl.thumbnail import ImageField


class OurTeam(models.Model):
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
        'contributors.TeamRole',
        verbose_name='роль в команде',
        on_delete=models.PROTECT,
    )
    contact = models.ManyToManyField(
        'contributors.MemberContact',
        'контакты',
    )

    class Meta:
        verbose_name = 'член команды'
        verbose_name_plural = 'члены команды'
        ordering = ('role',)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
