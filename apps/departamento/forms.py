from django import forms


class NuevoDepartamento(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    abreviatura = forms.CharField(max_length=20)
