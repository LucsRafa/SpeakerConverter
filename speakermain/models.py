from django.conf import settings
from django.db import models
from django.utils import timezone
import string, random
from django.contrib.auth.models import User

def gerarNomeInterno():
        carac_permitido = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choices(carac_permitido,k=20))

#def pegarusuario():
#  return User.request.user
modeloescolhas = (
    ('Vitoria','Vitória'),
    ('Ricardo','Ricardo'),
    ('Camila','Camila'),
    )
formatoescolhas = (('mp3','mp3'),('ogg','ogg'))
class SpeakFile(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)
    corpo = models.TextField(max_length=1000)
    modelo = models.CharField(verbose_name='Modelo de voz', max_length=50,choices=modeloescolhas,default='Camila')
    formato = models.CharField(max_length=4,choices=formatoescolhas,default='mp3')
    datacriado = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    NomeInterno = models.CharField(verbose_name='Nome Interno', max_length=20, default=gerarNomeInterno)
    CaminhoInterno = models.CharField(verbose_name='Caminho Interno', default='/media/Included/temp/', max_length=50)
    flagapi = models.BooleanField(default=False)
    
    def uparbanco(self):
        self.save()
        
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Arquivos de Voz'
        verbose_name_plural = 'Arquivos de Voz'