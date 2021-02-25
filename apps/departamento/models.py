from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Abreviatura', max_length=20)
    active = models.BooleanField('Activo', default=True, editable=True)

    class Meta:
        ordering = ['id']
        unique_together = ('name', 'short_name')
        # verbose_name = 'Nuestro departamento'
        # verbose_name = 'Nuestros departamentos'

    def __str__(self):
        return self.name + ' - ' + self.short_name
