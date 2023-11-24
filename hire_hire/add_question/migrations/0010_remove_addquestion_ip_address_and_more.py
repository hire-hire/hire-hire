# Generated by Django 4.2a1 on 2023-11-08 09:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0013_alter_questionlastdateused_options_and_more'),
        (
            'add_question',
            '0009_rename_user_cookie_addquestion_user_cookie_id_and_more',
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addquestion',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='addquestion',
            name='user_cookie_id',
        ),
        migrations.AlterField(
            model_name='addquestion',
            name='answer',
            field=models.TextField(
                max_length=500,
                validators=[django.core.validators.MinLengthValidator(2)],
                verbose_name='правильный ответ',
            ),
        ),
        migrations.AlterField(
            model_name='addquestion',
            name='author',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='add_questions',
                to=settings.AUTH_USER_MODEL,
                verbose_name='автор',
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addquestion',
            name='language',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='add_questions',
                to='interview.language',
                verbose_name='язык',
            ),
        ),
    ]