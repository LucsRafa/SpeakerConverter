from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaPrincipal, name='TelaPrincipal'),
    path('audio-detail/<int:pk>/', views.detalhesPrincipal, name='audio-detail'),
    path('login/',views.login_view, name='LoginView'),
    path('logout/', views.logout_view, name="LogoutView"),
    path('converter/', views.telaCoverter, name='teladeconverter'),
    ]
