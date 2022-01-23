from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from jovem.forms import DepoimentoForm
from .models import Depoimento
from empresa.models import Vagas
from jovem.forms import CandidatarForm
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def dashboard(request):
    info = Vagas.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'jovem/dashboard.html', {'info': info})


def perfil_jovem(request):
    return render(request, 'jovem/perfil_jovem.html')


def alterar_perfil(request):
    return render(request, 'jovem/alterar_perfil.html')


def login(request):
    if request.method != 'POST':
        return render(request, 'jovem/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.add_message(request, messages.ERROR, 'Usuario ou senha invalidos')
        return render(request, 'jovem/login.html')
    else:
        auth.login(request, user)
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('home')


def cadastrar(request):
    # validando se veio de um formulario POST
    if request.method != 'POST':
        return render(request, 'jovem/cadastrar.html')
    # obtendo os dados do form
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha = request.POST.get('senha')

    if not email or not usuario or not nome or not sobrenome or not senha:
        messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
        return render(request, 'jovem/cadastrar.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.WARNING, 'email inválido')
        return render(request, 'jovem/cadastrar.html')

    if len(senha) < 6:
        messages.add_message(request, messages.WARNING, 'Senha deve ter no mínimo 6 caracter')
        return render(request, 'jovem/cadastrar.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.WARNING, 'Usuário já existe')
        return render(request, 'jovem/cadastrar.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.WARNING, 'e-mail já existe')
        return render(request, 'jovem/cadastrar.html')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=nome,
        last_name=sobrenome,
        password=senha
    )
    messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
    user.save()
    return redirect('login')


def dicasjovem(request):
    return render(request, 'jovem/dicasjovem.html')


def curriculo(request):
    return render(request, 'jovem/curriculo.html')


def vagas_favoritas(request):
    return render(request, 'jovem/vagas_favoritas.html')


def empresasfavoritas(request):
    return render(request, 'jovem/empresasfavoritas.html')


def vagas_aberta(request):
    info = Vagas.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'jovem/vagas_favoritas.html', {'info': info})


def cadastro_Depoimento(request):
    if str(request.method) == 'POST':
        form = DepoimentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso!!')
        else:
            messages.error(request, 'Erro')
            form = DepoimentoForm()
            return render(request, 'jovem/cadastro_Depoimento.html', {'form': form})
    else:
        form = DepoimentoForm()
    dados = Depoimento.objects.all()
    contexto = {
        'form': form,
        'dados': dados,
    }
    return render(request, 'jovem/cadastro_Depoimento.html', contexto)


def view(request, pk):
    info = {}
    info['if'] = Vagas.objects.get(pk=pk)
    return render(request, 'jovem/vagas_aberta.html', info)


def candidato(request,pk):
    info = {}
    info['form_perfil'] = CandidatarForm()
    info['if'] = Vagas.objects.get(pk=pk)
    return render(request,'jovem/candidato.html',info)
    
def create_candidatar(request):
    form_perfil = CandidatarForm(request.POST or None)
    if form_perfil.is_valid():
        form_perfil.save()
        return redirect('dashboard')