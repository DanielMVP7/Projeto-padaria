from django.shortcuts import render, redirect
from .forms import ClienteForm, ProdutoForm, InfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'site/home.html')

@login_required(login_url='/login/')
def pedidos(request):
    form = ProdutoForm()
    context = {
            'form': form
        }
    return render(request, 'site/pedidos.html', context=context)

def infomacoes(request):
    form = InfoForm()
    context = {
            'form': form
        }
    return render (request, 'site/info.html', context=context)

def obrigado(request):
    return render(request, 'site/obrigado.html')

def login_cliente(request):
    return render(request, 'site/login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pedidos/')
        else:
            messages.error(request, 'E-mail e/ou senha inválidos. Favor tentar novamente.')
    return redirect('/login/')


def cadastre_se(request):
    if request.method == "GET":
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, 'site/cadastre-se.html', context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForm

        context = {
            'form': form
        }
        return render(request, 'site/cadastre-se.html', context=context)
