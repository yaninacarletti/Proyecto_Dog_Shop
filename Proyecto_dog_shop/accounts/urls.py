from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', logueo, name= 'Login'),
    path('register/', register, name= 'Register'),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name= 'Logout'),
    path('editarPerfil/', editarPerfil, name= 'EditarPerfil'),
    path('mostrarPerfil/', mostrarPerfil, name= 'MostrarPerfil'),
    path('eliminarPerfil/', eliminarPerfil, name= 'EliminarPerfil'),
    ]

