"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Configurações das variáveis de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Certifique-se de que o ambiente virtual está ativado antes de rodar este script

# Configuração do WSGI
application = get_wsgi_application()
