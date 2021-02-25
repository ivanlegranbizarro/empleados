from django import forms
from .models import Prueba

# Desde aquí personalizaremos nuestros 'form' de Django, para poder estilizar el HTML
# que DJANGO genera automáticamente por nosotros


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese un título'})
        }

        """ Aquí, por ejemplo, vamos a sobreescribir la validación del formulario
        para hacer que no nos valide cantidades menores a 10"""

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return cantidad
