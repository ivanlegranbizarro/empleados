from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'departamento', 'job',)
    search_fields = ('last_name',)
    list_filter = ('job', 'habilidades', 'departamento')
    filter_horizontal = ('habilidades',)

    # # Creamos la función 'full_name' para poder insertar esta columna que no existía en los modelos creados
    # def nombre_completo(self, obj):
    #     return obj.first_name + ' ' + obj.last_name


admin.site.register(Empleado, EmpleadoAdmin)
