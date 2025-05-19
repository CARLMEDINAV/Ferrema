from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'email', 'contraseña', 'telefono', 'direccion']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
