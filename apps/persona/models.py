from django.db import models
from apps.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.


class Habilidades(models.Model):
    habilidades = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Habilidades de nuestros empleados"
        verbose_name_plural = "Habilidades de nuestros empleados"

    def __str__(self):
        return self.habilidades


class Empleado(models.Model):
    """Modelo para la tabla de Empleado"""
    job_choices = (
        ('1', 'Contable'),
        ('2', 'Administrador'),
        ('3', 'Tesorero'),
        ('4', 'Otros'),
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=120)
    full_name = models.CharField('Nombre completo', max_length=255, blank=True)
    job = models.CharField('Puesto', max_length=50, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(
        'Avatar', upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    curriculum = RichTextField(null=True, blank=True)

    class Meta:
        ordering = ['id']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + ' - ' + self.last_name + ' - ' + self.job + ' - ' + str(self.departamento)
