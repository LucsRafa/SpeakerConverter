# Generated by Django 3.2.25 on 2024-06-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakermain', '0010_alter_speakfile_nomeinterno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakfile',
            name='NomeInterno',
            field=models.CharField(default='4FG0PsmKyVlUdq4EAUGr', max_length=20, verbose_name='Nome Interno'),
        ),
    ]
