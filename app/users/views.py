from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from emails.funcs import send_email
# Create your views here.

def verify_user(request, uuid):
    usuario = Usuario.objects.get(uuid=uuid)
    if usuario is not None:
        usuario.is_verified = True
        usuario.save()
        context = {'usuario': usuario}
        return render(request, 'users/verify.html', context)
    

def authenticate_user(request):
    form = AuthenticationForm()
    context = {'form': form}
    
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']

        if email is not None and password is not None:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                request.session['user_id'] = user.pk
                send_email(user.email, user.nome, user.codigo)
                return redirect('users:login_view')
            
            context['mensagem'] = 'Email ou senha invalidos'
            return render(request, 'users/authenticate.html', context)
            
    return render(request, 'users/authenticate.html', context)


def login_user(request):
    user_id = request.session['user_id']
    usuario = Usuario.objects.get(id=user_id)
    if request.method == 'POST':
        codigo = request.POST['codigo']
        
        if usuario is not None:
            if usuario.codigo.codigo == codigo:
                print('Sao iguais')
                login(request, usuario)
                usuario.codigo.save()
                return redirect('users:logado')
            else:
                print('nao sao iguais')
                return render(request, 'users/login.html', {'mensagem': 'Codigo invalido!'})
    
    context = {
        'nome': usuario.nome,
    }   
    return render(request, 'users/login.html', context)


def logado_view(request):
    user_id = request.session['user_id']
    usuario = Usuario.objects.get(id=user_id)
    return render(request, 'users/logado.html', {'nome': usuario.nome})
    
    
def logout(request):
    form = AuthenticationForm()
    return render(request, 'users/authenticate.html', {'form': form})