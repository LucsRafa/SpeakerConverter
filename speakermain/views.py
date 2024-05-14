from django.shortcuts import render

def telaPrincipal(request):
    return render(request, 'speakermain/index.html')