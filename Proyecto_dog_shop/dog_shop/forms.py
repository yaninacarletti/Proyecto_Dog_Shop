from django import forms
from .models import Producto, Servicio, Marca, LeerMasServicios

# class ProductoFormulario(forms.Form):

#     nombre = forms.CharField(max_length=50)
#     precio = forms.FloatField()
#     stock = forms.IntegerField()
#     imagen = forms.ImageField()

class ProductoFormulario(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ('__all__')


# class ServicioFormulario(forms.Form):

#     nombre = forms.CharField(max_length=50)
#     precio = forms.FloatField()
#     num_max_citas = forms.IntegerField()

class ServicioFormulario(forms.ModelForm):
    
    class Meta:
        model = Servicio
        fields = ('__all__')

class MarcaFormulario(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = ('__all__')

class LeerMasServiciosFormulario(forms.ModelForm):
    
    class Meta:
        model = LeerMasServicios
        fields = ('__all__')
