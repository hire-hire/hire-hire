# Generated by Django 4.2a1 on 2023-03-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('add_question', '0001_squashed_0007_alter_addquestion_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='addquestion',
            name='user_cookie',
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                verbose_name='user cookie id',
            ),
        ),
    ]
