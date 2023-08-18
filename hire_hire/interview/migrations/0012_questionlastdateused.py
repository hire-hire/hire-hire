# Generated by Django 4.2a1 on 2023-08-18 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0011_alter_question_answer_alter_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLastDateUsed',
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
                ('time', models.DateField(verbose_name='время использования')),
                (
                    'question',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='question_last_date_used',
                        to='interview.question',
                        verbose_name='вопрос',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='question_last_date_used',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='пользователь',
                    ),
                ),
            ],
            options={
                'verbose_name': 'последний раз использования вопроса',
                'verbose_name_plural': 'последний раз использования вопросов',
            },
        ),
    ]
