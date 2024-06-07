import boto3
from .models import SpeakFile
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import string
import random
from django.conf import settings

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess

def gerarN():
        carac_permitido = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choices(carac_permitido,k=20))

@receiver(post_save, sender=SpeakFile, dispatch_uid="AWSPolly")
def popularNome (sender, instance, created, **kwargs):
    sintetizar(instance)

def sintetizar (instance):
    caminho = os.path.join(settings.MEDIA_ROOT, "Included", "temp")
    objaudio = [instance.corpo, instance.formato, instance.modelo]
    session = Session(profile_name="SpeakerConverter")
    polly = session.client("polly")
    
    if objaudio[1] == 'ogg':
        nome = instance.NomeInterno+'.ogg'
        objaudio[1] = 'ogg_vorbis'
    else:
        nome = instance.NomeInterno+'.mp3'
    
    if instance.modelo == 'Vitória':
        instance.modelo = 'Vitoria'
    
    
    #DEBUG
    print('----------------------------------------------------------------------------------------------\nÁREA DE TESTES\n') 
    print('Caminho da pasta temp:', os.path.join(caminho))
    print('Nome do arquivo criado:', nome)
    print('Permissões:')
    print ('O arquivo existe?',os.access(caminho, os.F_OK ))
    print ('Ele pode ser lido?',os.access(caminho, os.R_OK))
    print ('Ele pode ser escrito?',os.access(caminho, os.W_OK))
    print ('Ele pode ser executado?',os.access(caminho, os.X_OK))
    try:
        response = polly.synthesize_speech(Text=objaudio[0], OutputFormat=objaudio[1], VoiceId=objaudio[2])
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
        
    streams = response['AudioStream']
    output = os.path.join(caminho, nome)
    with open (output, 'wb') as file:
        for chunk in streams:
            file.write(chunk)
        
post_save.connect(popularNome, sender=SpeakFile)