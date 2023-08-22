from django.contrib import admin
from .models import *


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    empty_value_display = '-No hay datos-'
    search_fields = ['nombre']
    list_display = ['nombre', 'total_mun', 'total_int']
    list_per_page = 15

    def total_int(self, obj):
        return obj.total_int

    total_int.short_description = 'Total de Institucion(es)'

    def total_mun(self, obj):
        return obj.total_mun

    total_mun.short_description = 'Total de Municipio(s)'


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    empty_value_display = '-No hay datos-'
    search_fields = ['provincia', 'nombre']
    list_display = ['provincia', 'nombre', 'total_int']
    list_filter = ['provincia']
    list_per_page = 15

    def total_int(self, obj):
        return obj.total_int

    total_int.short_description = 'Total de Institucion(es)'


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    empty_value_display = '-No hay datos-'
    search_fields = ['nombre']
    list_display = ['nombre', 'direccion', 'municipio', 'disponible']
    list_filter = ['municipio']
    list_editable = ['disponible']
    list_per_page = 15
    fields = ['nombre', 'direccion', 'provincia', 'municipio', 'disponible']


@admin.register(InstImagenes)
class ImagenesAdmin(admin.ModelAdmin):
    empty_value_display = '-No hay datos-'
    search_fields = ['nombre', 'descripcion']
    list_display = ['institucion', 'nombre', 'descripcion', 'disponible']
    list_editable = ['disponible']
    list_per_page = 15
