from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaPrincipal, name='TelaPrincipal')
]
