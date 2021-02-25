from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'
urlpatterns = [
    path('lista-departamentos/', views.ListaDepartamentoView.as_view(),
         name='lista_departamentos'),
    path('nuevo-departamento/', views.VistaNuevoDepartamento.as_view(),
         name='nuevo_departamento'),
]
