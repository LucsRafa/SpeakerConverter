from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import reset_password_form

urlpatterns = [
    path('', views.telaPrincipal, name='TelaPrincipal'),
    path('audio-detail/<int:pk>/', views.detalhesPrincipal, name='audio-detail'),
   path('login/',views.login_view, name='LoginView'),
    path('logout/', views.logout_view, name="LogoutView"),
    path('converter/', views.telaCoverter, name='teladeconverter'),
    path('delete-file/', views.delete_file, name='delete_file'),
    path("register/", views.register_view, name="register"),
    path('empresa/', views.empresa_view, name='empresa'),
    path('contato/', views.contato_view, name='contato'),
    path('reset_password_form/', reset_password_form, name='reset_password_form'),
    path('excluir-conta/', views.ExcluirContaView.as_view(), name='ExcluirContaView'),
]
