import os
import random
from django.db import models


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'inst_img/{basename}{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr,
                                                           ext=file_extension)


class Provincia(models.Model):
    nombre = models.CharField(max_length=32, unique=True, blank=False, null=False)
    total_mun = property(lambda self: self.municipio.count())
    total_int = property(lambda self: self.institucion.count())

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Municipio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='municipio')
    nombre = models.CharField(max_length=32, unique=True, blank=False, null=False)
    total_int = property(lambda self: self.institucion.count())

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Institucion(models.Model):
    nombre = models.CharField(max_length=64, blank=False, null=False)
    direccion = models.CharField(max_length=150)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='institucion')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='institucion')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class InstImagenes(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='imagenes')
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(u'Descripción', help_text='Descripción de la Imagen.')
    photo = models.ImageField('Imagen', upload_to=photo_path, help_text='Imágenes del lugar.')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
