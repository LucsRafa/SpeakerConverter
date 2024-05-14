from django.conf import settings
from django.db import models
from django.utils import timezone

class SpeakFile(models.Model):
    identificador = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    corpo = models.TextField(max_length=1000)
    modelo = models.CharField(verbose_name='Modelo de voz', max_length=50)
    formato = models.CharField(max_length=4)
    datacriado = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    
    def uparbanco(self):
        self.save()
        
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Arquivos de Voz'
        verbose_name_plural = 'Arquivos de Voz'