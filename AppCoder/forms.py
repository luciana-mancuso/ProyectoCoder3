from django import forms

class ProductoForm(forms.Form):
    nombre=forms.CharField(min_length=3, max_length=40)
    precio=forms.IntegerField(min_value=1)


class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)

class BusquedaUsuarioForm(forms.Form):
    apellido=forms.CharField(max_length=30)