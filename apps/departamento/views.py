from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NuevoDepartamento
from apps.persona.models import Empleado
from .models import Departamento

# Create your views here.


class ListaDepartamentoView(ListView):
    template_name = "departamento/lista_departamentos.html"
    model = Departamento
    context_object_name = 'departamentos'


class VistaNuevoDepartamento(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamento
    success_url = '/'

    def form_valid(self, form):
        depart = Departamento(
            name=form.cleaned_data['departamento'], short_name=form.cleaned_data['abreviatura'])
        depart.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre, last_name=apellidos, job='1', departamento=depart)
        # Con la función create no necesito hacer un '.save()'
        return super(VistaNuevoDepartamento, self).form_valid(form)
