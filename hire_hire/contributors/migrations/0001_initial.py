# Generated by Django 4.2a1 on 2023-02-21 14:25

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='MemberContact',
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
                (
                    'social_network',
                    models.CharField(max_length=150, verbose_name='название соцсети'),
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
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.CreateModel(
            name='TeamRole',
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
                ('name', models.CharField(max_length=150, verbose_name='название')),
            ],
            options={
                'verbose_name': 'роль',
                'verbose_name_plural': 'роли',
            },
        ),
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
                        help_text='Добавьте фото', upload_to='team', verbose_name='фото'
                    ),
                ),
                (
                    'contact',
                    models.ManyToManyField(
                        related_name='контакты', to='contributors.membercontact'
                    ),
                ),
                (
                    'role',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='contributors.teamrole',
                        verbose_name='роль в команде',
                    ),
                ),
            ],
            options={
                'verbose_name': 'член команды',
                'verbose_name_plural': 'члены команды',
                'ordering': ('role',),
            },
        ),
    ]