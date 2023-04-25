from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserEditForm
from django.contrib.auth.models import User
from .models import Avatar

# Create your views here.

def logueo(request):
    if request.method == "POST":
            miFormulario = AuthenticationForm(request, data=request.POST)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                usuario = data['username']
                psw = data['password']

                user = authenticate(username=usuario, password=psw)

                if user:
                    login(request, user)
                    try:
                        avatar = Avatar.objects.get(user = request.user.id)
                        return render(request, 'inicio.html',{'mensaje': f'Bienvenido {usuario.capitalize()}', 'url': avatar.imagen.url})
                    except:
                        return render(request, 'inicio.html',{'mensaje': f'Bienvenido {usuario.capitalize()}'})
                else:
                    return render(request, 'inicio.html',{'mensaje':'Error: datos incorrectos'})
                
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, "login.html", {"miFormulario": miFormulario})

def register(request):
    if request.method == "POST":
            miFormulario = UserCreationForm(request.POST)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                username = data['username']
                miFormulario.save()
                return render(request, 'inicio.html',{'mensaje': f'Usuario {username} creado exitósamente'})
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = UserCreationForm()
        return render(request, "registro.html", {"miFormulario": miFormulario})

@login_required  
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
            miFormulario = UserEditForm(request.POST, instance= request.user)
            if miFormulario.is_valid(): 
                data = miFormulario.cleaned_data
                usuario.first_name = data["first_name"]
                usuario.last_name = data["last_name"]
                usuario.email = data["email"]
                usuario.set_password(data['password1'])
                usuario.save()
                return render(request, "inicio.html", {'mensaje': 'Datos actualizados correctamente'})
            else:
                return render(request, "inicio.html", {"miFormulario": miFormulario})
    else:
        miFormulario = UserEditForm(instance = request.user)
        return render(request, "editarPerfil.html", {"miFormulario": miFormulario})

@login_required  
def mostrarPerfil(request):
    usuario = request.user
    miFormulario = UserEditForm(instance = usuario)
    return render(request, "mostrarPerfil.html", {"miFormulario": miFormulario})

@login_required  
def eliminarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        usuario.delete()
        return render(request, "inicio.html", {'mensaje': 'Perfil eliminado correctamente'})
    return render(request, 'eliminarPerfil.html')


