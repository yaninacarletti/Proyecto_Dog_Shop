from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Contacto, Avatar

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ("__all__")

# class AvatarFormulario(forms.Form):

#     user = forms.CharField()   debe ser un tipo de instancia USER
#     imagen = forms.ImageField()

    def clean_user(self):
        user = self.cleaned_data['user']
        if user != self.user.username:
            raise forms.ValidationError("Sólo puede modificar su propio avatar")
        return user
        

class ContactoFormulario(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ('__all__')


class UserEditForm(UserChangeForm):

    password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False)

    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2


