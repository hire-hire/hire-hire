# Generated by Django 4.2a1 on 2023-06-01 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('duel', '0002_alter_duel_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duelplayer',
            options={
                'ordering': ['pk'],
                'verbose_name': 'участник дуэли',
                'verbose_name_plural': 'участники дуэли',
            },
        ),
    ]
