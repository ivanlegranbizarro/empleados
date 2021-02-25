from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view()),
    path('lista-empleados/', views.ListaTodosEmpleados.as_view(),
         name="lista_empleados"),
    path('lista-empleados-por-departamento/<name>/',
         views.ListaAreaEmpleados.as_view(), name="empleados_por_departamento"),
    path('buscar-empleados/', views.ListaTextoEmpleados.as_view()),
    path('habilidades-empleados/<id>/',
         views.ListaHabilidadesEmpleados.as_view()),
    path('detalle-empleados/<pk>/',
         views.DetalleEmpleados.as_view(), name="detalle_empleado"),
    path('add-empleado/', views.EntradaUsuarios.as_view(), name="add_empleado"),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('editar_empleado/<pk>/',
         views.EditarEmpleado.as_view(), name='editar_empleado'),
    path('eliminar/<pk>/', views.EliminarEmpleado.as_view(),
         name='eliminar_empleado'),
    path('admin_empleados/', views.ListaAdminEmpleados.as_view(),
         name='admin_empleados'),
]
