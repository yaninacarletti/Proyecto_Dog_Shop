from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Servicio
from .forms import ProductoFormulario, ServicioFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

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

def servicioFormulario(request):
    if request.method == "POST":
            miFormulario = ServicioFormulario(request.POST)
            #print(miFormulario)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                servicios = Servicio(nombre=data["nombre"], precio=data["precio"], num_max_citas=data["num_max_citas"])
                servicios.save()
                return render(request, "inicio.html")
    else:
        miFormulario = ServicioFormulario()
        return render(request, "servicioFormulario.html", {"miFormulario": miFormulario})

def busqueda_stock(request):
    return render(request, 'busqueda_stock.html')

def buscar(request):
    if request.GET['stock']:
        stock = request.GET['stock']
        productos = Producto.objects.filter(stock__icontains=stock)
        return render(request, "resultado_busqueda_stock.html", {"productos": productos, "stock":stock})
    else:
        respuesta ="No enviaste datos"
        return HttpResponse(respuesta)

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

def listaProductos(request):
    try:
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos':productos, 'url':productos.imagen.url})
    except:
        return render(request, 'productos.html', {'productos':productos})

def detalleProductos(request, id):
    producto = Producto.objects.get(id = id)
    return render(request, 'detalleProducto.html', {'producto':producto})

@staff_member_required
def crearProducto(request):
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                producto = Producto(nombre=data["nombre"], precio=data["precio"], stock=data["stock"])
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
        productos = Producto.objects.all()
        return render(request, 'productoList.html', {'productos':productos})
    return render(request, 'productoDelete.html')
    
@staff_member_required
def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST)
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





