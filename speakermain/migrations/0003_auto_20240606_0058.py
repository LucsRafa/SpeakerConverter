# Generated by Django 3.2.25 on 2024-06-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakermain', '0002_alter_speakfile_nomeinterno'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakfile',
            name='flagapi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='speakfile',
            name='NomeInterno',
            field=models.CharField(max_length=20, verbose_name='Nome Interno'),
        ),
    ]
