from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import SpeakFile
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import formSpeakFile

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
    return redirect(telaPrincipal)

@login_required
def telaCoverter (request):
    if request.method == 'POST':
        form = formSpeakFile(request.POST)
        if form.is_valid():
            form.instance.autor = request.user
            form.instance.NomeInterno = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            form.save()
            return redirect(telaPrincipal)
    else:
        form = formSpeakFile()
    return render(request, 'speakermain/telaConverter.html', {'form':    form})