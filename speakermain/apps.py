from django.apps import AppConfig
from django.db.models.signals import post_save


class SpeakermainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'speakermain'
    def ready(self):
        from .models import SpeakFile
        from .api_calls import popularNome
        post_save.connect(popularNome, sender=SpeakFile)