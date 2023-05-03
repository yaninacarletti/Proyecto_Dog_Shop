from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserEditForm, ContactoFormulario, AvatarFormulario
from django.contrib.auth.models import User
from .models import Avatar, Contacto
from datetime import datetime
import calendar
import time

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
                        return render(request, 'Bienvenida.html', {'url': avatar.imagen.url})
                    except:
                        return render(request, 'Bienvenida.html')
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
                username = data['username'].capitalize()
                miFormulario.save()
                return render(request, 'creacionUsuario.html', {"username":username})
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
                return render(request, "editarDevolucion.html")
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

#CONTACTO
def crearContacto(request):
    fecha = datetime.now().date()
    contacto = Contacto(fecha = fecha)
    fecha = time.gmtime()
    time_stamp = calendar.timegm(fecha)
    fecha = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d')
    if request.method == "POST":
        contacto = Contacto(nombre=request.POST["nombre"], correo=request.POST["correo"], asunto=request.POST["asunto"], mensaje=request.POST["mensaje"], fecha = fecha)
        contacto.save()
        return render(request, "contacto_devolucion.html")
    else:
        return render(request, "contacto.html", {"contacto": contacto})
    
def busquedaContacto(request):
    return render(request, 'busquedaContacto.html')

def buscar(request):
    if request.GET['fecha']:
        fecha = request.GET['fecha']
        contactos = Contacto.objects.filter(fecha__icontains=fecha)
        if contactos:
            return render(request, "resultadoBusquedaContacto.html", {"contactos": contactos, "fecha":fecha})
        else:
            return render(request, "noHayMensajes.html", {"fecha":fecha})
    else:
        respuesta ="No enviaste datos"
        return HttpResponse(respuesta)
    
#AVATAR
def crearAvatar(request):
    avatares = Avatar.objects.all()
    if request.method == "POST":
            miFormulario = AvatarFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                avatar = Avatar(user=data["user"], imagen=data["imagen"])
                avatar.save()
                return render(request, "avatares.html", {"avatar": avatar})
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = AvatarFormulario()
        return render(request, "avatarFormulario.html", {"miFormulario": miFormulario})
    
    