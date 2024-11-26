from django.urls import path
from . import views
from .views import register_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.telaPrincipal, name='TelaPrincipal'),
    path('audio-detail/<int:pk>/', views.detalhesPrincipal, name='audio-detail'),
    path('login/',views.login_view, name='LoginView'),
    path('logout/', views.logout_view, name="LogoutView"),
    path('converter/', views.telaCoverter, name='teladeconverter'),
    path('delete-file/', views.delete_file, name='delete_file'),
    path("register/", views.register_view, name="register"),
    ]