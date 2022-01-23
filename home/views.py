from django.shortcuts import render
from jovem.models import Depoimento


def index(request):
    dados = Depoimento.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados': dados})

def lei(request):
    return render(request, 'home/leiaprendiz.html')

def parceiros(request):
    return render(request, 'home/parceiros.html')

def sobre(request):
    return render(request, 'home/sobrenos.html')

def dicas(request):
    return render(request, 'home/dicas.html')

def op(request):
    return render(request, 'home/op.html')

def op_login(request):
    return render(request, 'home/op_login.html')

def gerador(request):
    return render(request, 'home/gerador.html')


def mostraDepoimento(request):
    dados = cadastro_Depoimento.objects.order_by('-id').filter(
        mostrar=True
    )
    print(dados)
    return render(request, 'home/index.html', {'dados': dados})
