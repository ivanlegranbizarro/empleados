from django.db import models

# Create your models here.


class Prueba(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    subtitulo = models.CharField(max_length=100, verbose_name='Subtítulo')
    cantidad = models.IntegerField(default=1, verbose_name='Cantidad')

    def __str__(self):
        return self.titulo + " | " + str(self.cantidad)
