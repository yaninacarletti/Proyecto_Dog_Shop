from django import forms

class ProductoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()
    stock = forms.IntegerField()

class ServicioFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()
    num_max_citas = forms.IntegerField()
