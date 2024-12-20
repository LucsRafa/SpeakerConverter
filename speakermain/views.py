from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import SpeakFile
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import formSpeakFile
from django.views.decorators.csrf import csrf_exempt  # Aqui está a importação que estava faltando
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

import random
import string

@login_required
def telaPrincipal(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    sfile = SpeakFile.objects.filter(autor=user, datacriado__lte=timezone.now()).order_by('-datacriado')
    return render(request, 'speakermain/index.html', {'sfile': sfile})

def detalhesPrincipal(request, pk):
    objaudio = get_object_or_404(SpeakFile, pk=pk)
    data = {
        'nome': objaudio.titulo,
        'corpo': objaudio.corpo,
        'datacriado': objaudio.datacriado,
        'modelo': objaudio.modelo,
        'caminho': f"{objaudio.CaminhoInterno}{objaudio.NomeInterno}.{objaudio.formato}"
    }
    return JsonResponse(data)
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect(telaPrincipal)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(telaPrincipal)
    else:
        form = AuthenticationForm()
    return render(request, 'speakermain/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('TelaPrincipal')

@login_required
def telaCoverter(request):
    if request.method == 'POST':
        form = formSpeakFile(request.POST)
        if form.is_valid():
            form.instance.autor = request.user
            form.instance.NomeInterno = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            form.save()
            return redirect(telaPrincipal)
    else:
        form = formSpeakFile()
    return render(request, 'speakermain/telaConverter.html', {'form': form})

@csrf_exempt  # Permite requisições sem CSRF para testes (use com cuidado em produção)
def delete_file(request):
    if request.method == 'POST':
        file_id = request.POST.get('id')
        try:
            file = SpeakFile.objects.get(id=file_id)
            file.delete()  # Exclui o arquivo do banco de dados
            return JsonResponse({'status': 'success', 'message': 'Arquivo excluído com sucesso!'})
        except SpeakFile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Arquivo não encontrado!'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método inválido!'}, status=400)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Autentica o novo usuário
            return redirect('TelaPrincipal')  # Redireciona para a página principal ou dashboard
        else:
            # Exibindo os erros no console para depuração
            print(form.errors)  # Isso vai mostrar os erros no console para você entender o que deu errado

           
    else:
        form = RegisterForm()

    return render(request, "speakermain/register.html", {"form": form})


def empresa_view(request):
    # Se o usuário já estiver autenticado, redireciona para a tela principal
    if request.user.is_authenticated:
        return redirect('TelaPrincipal')  # Substitua pelo nome correto da URL da tela principal

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('TelaPrincipal')  # Redireciona para a tela principal após login bem-sucedido
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Erro ao processar o formulário. Verifique as informações e tente novamente.")
    else:
        form = AuthenticationForm()

    # Renderiza a página com o formulário
    return render(request, 'speakermain/empresa.html', {'form': form})

def contato_view(request):
    # Se o usuário já estiver autenticado, redireciona para a tela principal
    if request.user.is_authenticated:
        return redirect('TelaPrincipal')  # Substitua pelo nome correto da URL

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('TelaPrincipal')  # Redireciona após login
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Erro ao processar o formulário. Verifique as informações e tente novamente.")
    else:
        form = AuthenticationForm()

    return render(request, 'speakermain/contato.html', {'form': form})

def reset_password_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
        else:
            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Senha redefinida com sucesso!')
                return redirect('login')  # Substitua 'login' pelo nome correto da sua rota de login
            except User.DoesNotExist:
                messages.error(request, 'Usuário não encontrado.')

    return render(request, 'speakermain/reset_password_form.html')

class ExcluirContaView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        user.delete()
        return redirect('TelaPrincipal')  