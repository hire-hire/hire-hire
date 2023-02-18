# Generated by Django 4.2a1 on 2023-02-18 12:54

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                (
                    'middle_name',
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name='отчество'
                    ),
                ),
                (
                    'photo',
                    sorl.thumbnail.fields.ImageField(
                        help_text='Добавьте фото', upload_to='', verbose_name='фото'
                    ),
                ),
                (
                    'role',
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, 'гуру проекта'),
                            (1, 'менеджеры проекта'),
                            (2, 'фронтенд разработчики'),
                            (3, 'бэкенд-разработчики'),
                            (4, 'QA-тестировщики'),
                            (5, 'UX/UI-дизайнеры'),
                        ],
                        verbose_name='роль в команде',
                    ),
                ),
                (
                    'contact',
                    models.URLField(
                        blank=True,
                        help_text='Укажите ссылку (github, telegram, vk и другие)',
                        null=True,
                        verbose_name='контакт',
                    ),
                ),
            ],
            options={
                'verbose_name': 'информация о команде',
                'verbose_name_plural': 'информация о команде',
                'ordering': ('role',),
            },
        ),
    ]