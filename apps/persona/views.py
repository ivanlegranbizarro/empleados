from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado

# Create your views here.


class ListaTodosEmpleados(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 4
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
        return lista


class ListaAreaEmpleados(ListView):
    template_name = 'persona/lista_area_empleados.html'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(departamento__name=area)
        return lista


class ListaTextoEmpleados(ListView):
    """Lista de empleados a través de una palabra de búsqueda."""
    template_name = 'persona/lista_texto_empleados.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista


class ListaHabilidadesEmpleados(ListView):
    template_name = 'persona/lista_habilidades_empleados.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.kwargs['id']
        empleado = Empleado.objects.get(id=id_empleado)
        return empleado.habilidades.all()


class DetalleEmpleados(DetailView):
    model = Empleado
    template_name = 'persona/detalle_empleados.html'
    context_object_name = 'empleados'


class SuccessView(TemplateView):
    template_name = 'persona/success_url.html'


class EntradaUsuarios(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job',
              'departamento', 'habilidades', 'avatar', ]
    success_url = reverse_lazy('persona_app:lista_empleados')

    """Prueba modificando el form valid interviniéndolo para añadir el método 'full_name'"""

    # def form_valid(self, form):
    #     empleado = form.save(commit=False)
    #     empleado.full_name = empleado.first_name + ' ' + empleado.last_name
    #     empleado.save()
    #     return super(EntradaUsuarios, self).form_valid(form)


class EditarEmpleado(UpdateView):
    template_name = 'persona/editar_empleado.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:admin_empleados')

    """ También, en lugar de intervenir el método form_valid, podemos modificar el método post
    para modificar/añadir características antes de salvar información validada"""

    """ Podemos modificar el objeto request con sus datos para modificar los datos enviados por método POST"""

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     print(request.POST)
    #     print(request.POST['first_name'])
    #     return super.post(request, *args, **kwargs)


class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'persona/eliminar_empleado.html'
    success_url = reverse_lazy('persona_app:admin_empleados')
    context_object_name = 'empleado'


class InicioView(TemplateView):
    """ Vista inicial de la página """
    template_name = 'persona/inicio.html'


class ListaAdminEmpleados(ListView):
    template_name = 'persona/admin_empleados.html'
    paginate_by = 10
    context_object_name = 'empleados'
    model = Empleado
