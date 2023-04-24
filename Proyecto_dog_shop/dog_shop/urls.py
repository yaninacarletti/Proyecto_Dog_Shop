from django.urls import path
from dog_shop.views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('quienes_somos/', quienes_somos, name= "Quienes_somos"),
    path('servicios/', servicios, name= "Servicios"),
    path('productos/', productos, name= "Productos"),
    path('contacto/', contacto, name= "Contacto"),
    # path('productoFormulario/', productoFormulario, name= "ProductoFormulario"),
    path('servicioFormulario/', servicioFormulario, name= "ServicioFormulario"),
    # path('cuentaFormulario/', cuentaFormulario, name= "CuentaFormulario"),    
    path('busqueda_stock/', busqueda_stock, name= "Busqueda_stock"),
    path('buscar/', buscar, name= "Buscar"),
    # path('listaProducto/', ProductoList.as_view(), name= "ListaProducto"),
    # path('detalleProducto/<pk>/', ProductoDetail.as_view(), name= "DetalleProducto"),
    # path('crearProducto/', ProductoCreate.as_view(), name= "CrearProducto"),
    # path('actualizarProducto/<pk>/', ProductoUpdate.as_view(), name= "ActualizarProducto"),
    # path('eliminarProducto/<pk>/', ProductoDelete.as_view(), name= "EliminarProducto"),
    path('listaProducto/', listaProductos, name= "ListaProducto"),
    path('crearProducto/', crearProducto, name= "CrearProducto"),
    path('eliminarProducto/<int:id>/', eliminarProducto, name= "EliminarProducto"),  
    path('editarProducto/<int:id>/', editarProducto, name= "EditarProducto"), 
    path('detalleProductos/<int:id>/', detalleProductos, name= "DetalleProductos")    
]


