# Generated by Django 3.2.25 on 2024-05-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakermain', '0003_auto_20240513_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakfile',
            name='identificador',
            field=models.IntegerField(default=0),
        ),
    ]
