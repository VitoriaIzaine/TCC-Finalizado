from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from empresa.forms import VagasForm
from empresa.forms import PerfilForm
from empresa.models import Vagas, Perfil_empresa
from jovem.models import Candidatar
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login_empresa')
def principal(request):
    return render(request, 'empresa/pagina_inicial.html')


def alterar_vagas(request):
    data = {}
    data['db'] = Vagas.objects.all()
    return render(request, 'empresa/alterar_vagas.html', data)


def perfil_empresa(request):
    info = {}
    info['pf'] = Perfil_empresa.objects.all()
    return render(request, 'empresa/perfil_empresa.html', info)


def logout(request):
    auth.logout(request)
    return redirect('home')


def cadastro_empresa(request):
    if request.method != 'POST':
        return render(request, 'empresa/cadastrar_empresa.html')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    if not email or not usuario or not nome or not senha:
        messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
        return render(request, 'empresa/cadastrar_empresa.html')
    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.WARNING, 'email inválido')
        return render(request, 'empresa/cadastrar_empresa.html')

    if len(senha) < 6:
        messages.add_message(request, messages.WARNING, 'Senha deve ter no mínimo 6 caracter')
        return render(request, 'empresa/cadastrar_empresa.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.WARNING, 'Usuário já existe')
        return render(request, 'empresa/cadastrar_empresa.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.WARNING, 'e-mail já existe')
        return render(request, 'empresa/cadastrar_empresa.html')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=nome,
        password=senha)
    messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
    user.save()
    return redirect('login_empresa')


def login_empresa(request):
    if request.method != 'POST':
        return render(request, 'empresa/login_empresa.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.add_message(request, messages.ERROR, 'Usuario ou senha invalidos')
        return render(request, 'empresa/login_empresa.html')
    else:
        auth.login(request, user)
        return redirect('principal')


def form(request):
    data = {}
    data['form'] = VagasForm()
    return render(request, 'empresa/cadastro_vagas.html', data)


def form_perfil(request):
    info = {}
    info['form_perfil'] = PerfilForm()
    return render(request, 'empresa/alterarperfil_Empresa.html', info)


def create_empresa(request):
    form_perfil = PerfilForm(request.POST or None)
    if form_perfil.is_valid():
        form_perfil.save()
        return redirect('principal')


def create(request):
    form = VagasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form')


def edit(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    data['form'] = VagasForm(instance=data['db'])
    return render(request, 'empresa/cadastro_vagas.html', data)


def update(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    form = VagasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('form')


def delete(request, pk):
    db = Vagas.objects.get(pk=pk)
    db.delete()
    return redirect('form')

def view_empresa(request, pk):
    teste = {}
    teste['ts']=Candidatar.objects.filter(id_vagaa = pk)
    return render(request, 'empresa/candidatos_empresa.html', teste)

def view_candidato(request, pk):
    teste = {}
    teste['ts'] = Candidatar.objects.get(pk=pk)
    return render(request, 'empresa/ver_candidato.html', teste)

