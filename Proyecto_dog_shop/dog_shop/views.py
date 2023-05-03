from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Servicio, Marca, LeerMasServicios
from .forms import ProductoFormulario, ServicioFormulario, MarcaFormulario, LeerMasServiciosFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# def inicio(request):
#     return render(request, 'inicio.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def servicios(request):
    return render(request, 'servicios.html')

def productos(request):
    return render(request, 'productos.html')

def contacto(request):
    return render(request, 'contacto.html')

# def productoFormulario(request):
#     if request.method == "POST":
#             miFormulario = ProductoFormulario(request.POST)
#             #print(miFormulario)
#             if miFormulario.is_valid():
#                 data = miFormulario.cleaned_data
#                 producto = Producto(nombre=data["nombre"], precio=data["precio"], stock=data["stock"])
#                 producto.save()
#                 return render(request, "inicio.html")
#     else:
#         miFormulario = ProductoFormulario()
#         return render(request, "productoFormulario.html", {"miFormulario": miFormulario})


# class ProductoList(ListView):
#     model = Producto
#     template_name = 'productoList.html'
#     context_object_name = 'productos'

# class ProductoDetail(DetailView):
#     model: Producto
#     template_name = 'productoDetail.html'
#     context_object_name = 'producto'

# class ProductoCreate(CreateView):
#     model: Producto
#     template_name = 'productoCreate.html'
#     fields = ('__all__')
#     success_url = "{% url 'Inicio'%}"

# class ProductoUpdate(UpdateView):
#     model: Producto
#     template_name = 'productoUpdate.html'   
#     fields = ('__all__')
#     success_url = "{% url 'Inicio'%}"
#     context_object_name = 'producto'

# class ProductoDelete(DeleteView):
#     model: Producto
#     template_name = 'productoDelete.html'
#     success_url = "{% url 'Inicio'%}"      

# PRODUCTOS
def listaProductos(request):
    try:
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos':productos})
    except:
        return render(request, 'productos.html', {'productos':productos})

def detalleProductos(request, id):
    producto = Producto.objects.get(id = id)
    return render(request, "detalleProducto.html", {"producto": producto})

@staff_member_required
def crearProducto(request):
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST,  request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                producto = Producto(nombre=data["nombre"], precio=data["precio"], stock=data["stock"], descripcion=data["descripcion"], imagen=data["imagen"])
                producto.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = ProductoFormulario()
        return render(request, "productoFormulario.html", {"miFormulario": miFormulario})

@staff_member_required
def eliminarProducto(request, id):
    if request.method == "POST":
        producto = Producto.objects.get(id=id)
        producto.delete()
        return HttpResponseRedirect('/dog_shop/listaProducto/')
    return render(request, 'productoDelete.html')
    
@staff_member_required
def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                producto.nombre = data["nombre"]
                producto.precio = data["precio"]
                producto.stock = data["stock"]
                producto.imagen = data["imagen"]
                producto.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = ProductoFormulario(initial ={
            'nombre': producto.nombre,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagen': producto.imagen
        })
        return render(request, "editarFormulario.html", {"miFormulario": miFormulario, "id": producto.id})
    
#SERVICIOS
def listaServicios(request):
    try:
        servicios = Servicio.objects.all()
        return render(request, 'servicios.html', {'servicios':servicios})
    except:
        return render(request, 'servicios.html', {'servicios':servicios})

def detalleServicios(request, id):
    servicio = Servicio.objects.get(id = id)
    return render(request, 'detalleServicio.html', {'servicio':servicio})

@staff_member_required
def crearServicio(request):    
    if request.method == "POST":
            miFormulario = ServicioFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                servicios = Servicio(nombre=data["nombre"], precio=data["precio"], num_max_citas=data["num_max_citas"])
                servicios.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = ServicioFormulario()
        return render(request, "servicioFormulario.html", {"miFormulario": miFormulario})
    
@staff_member_required
def eliminarServicio(request, id):
    if request.method == "POST":
        servicio = Servicio.objects.get(id=id)
        servicio.delete()
        return HttpResponseRedirect('/dog_shop/listaServicio/')
    return render(request, 'servicioDelete.html')
    
@staff_member_required
def editarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    if request.method == "POST":
            miFormulario = ServicioFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                servicio.nombre = data["nombre"]
                servicio.precio = data["precio"]
                servicio.num_max_citas = data["num_max_citas"]
                servicio.imagen = data["imagen"]
                servicio.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = ServicioFormulario(initial ={
            'nombre': servicio.nombre,
            'precio': servicio.precio,
            'num_max_citas': servicio.num_max_citas,
            'imagen': servicio.imagen
        })
        return render(request, "editarFormularioServicio.html", {"miFormulario": miFormulario, "id": servicio.id})
    
#MARCAS
def listaMarcas(request):
    try:
        marcas = Marca.objects.all()
        return render(request, 'marcas.html', {'marcas':marcas})
    except:
        return render(request, 'marcas.html', {'marcas':marcas})

@staff_member_required
def crearMarca(request):
    if request.method == "POST":
            miFormulario = MarcaFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                marca = Marca(nombre=data["nombre"], imagen=data["imagen"])
                marca.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = MarcaFormulario()
        return render(request, "marcaFormulario.html", {"miFormulario": miFormulario})

@staff_member_required
def eliminarMarca(request, id):
    if request.method == "POST":
        marca = Marca.objects.get(id=id)
        marca.delete()
        return HttpResponseRedirect('/dog_shop/listaMarcas/')
    return render(request, 'marcaDelete.html')
    
@staff_member_required
def editarMarca(request, id):
    marca = Marca.objects.get(id=id)
    if request.method == "POST":
            miFormulario = MarcaFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                marca.nombre = data["nombre"]
                marca.imagen = data["imagen"]
                marca.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = MarcaFormulario(initial ={
            'nombre': marca.nombre,
            'imagen': marca.imagen
        })
        return render(request, "editarFormularioMarca.html", {"miFormulario": miFormulario, "id": marca.id})
        
#LEER MAS SERVICIOS
def leerMasServicios(request, id):
    lms = LeerMasServicios.objects.get(id = id)
    return render(request, 'leerMasServicios.html', {'lms':lms})

# @staff_member_required
# def crearLeerMasServicios(request):
#     if request.method == "POST":
#             miFormulario = LeerMasServiciosFormulario(request.POST)
#             if miFormulario.is_valid():
#                 data = miFormulario.cleaned_data
#                 leerMasServicios = LeerMasServicios(titulo=data["titulo"], subtitulo=data["subtitulo"], descripcion=data["descripcion"], imagen=data["imagen"],)
#                 leerMasServicios.save()
#                 return HttpResponseRedirect('/dog_shop/')
#             else:
#                 return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
#     else:
#         miFormulario = LeerMasServiciosFormulario()
#         return render(request, "leerMasServiciosFormulario.html", {"miFormulario": miFormulario})
    
@staff_member_required
def eliminarLeerMasServicios(request, id):
    if request.method == "POST":
        leerMasServicios = LeerMasServicios.objects.get(id=id)
        leerMasServicios.delete()
        return HttpResponseRedirect('/dog_shop/ListaServicio/')
    return render(request, 'leerMasServiciosDelete.html')   

@staff_member_required
def editarLeerMasServicios(request, id):
    leerMasServicios = LeerMasServicios.objects.get(id=id)
    if request.method == "POST":
            miFormulario = LeerMasServiciosFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                leerMasServicios.titulo = data["titulo"]
                leerMasServicios.subtitulo = data["subtitulo"]
                leerMasServicios.descripcion = data["descripcion"]
                leerMasServicios.imagen = data["imagen"]
                leerMasServicios.save()
                return HttpResponseRedirect('/dog_shop/')
            else:
                return render(request, "inicio.html", {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = LeerMasServiciosFormulario(initial ={
            'titulo': leerMasServicios.titulo,
            'subtitulo': leerMasServicios.subtitulo,
            'descripcion': leerMasServicios.descripcion,
            'imagen': leerMasServicios.imagen
        })
        return render(request, "editarFormularioLeerMasServicios.html", {"miFormulario": miFormulario, "id": leerMasServicios.id})
        
def inicio(request):
    servicios = Servicio.objects.all()
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'inicio.html', {'servicios':servicios, 'productos':productos, 'marcas':marcas})



