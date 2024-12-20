# Generated by Django 3.2.25 on 2024-05-14 02:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('speakermain', '0002_alter_speakfile_corpo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakfile',
            options={'verbose_name': 'Arquivos de Voz', 'verbose_name_plural': 'Arquivos de Voz'},
        ),
        migrations.AlterField(
            model_name='speakfile',
            name='datacriado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='speakfile',
            name='formato',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='speakfile',
            name='modelo',
            field=models.CharField(max_length=50, verbose_name='Modelo de voz'),
        ),
    ]
