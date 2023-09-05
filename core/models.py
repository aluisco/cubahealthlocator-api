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
    descripcion_es = models.TextField(u'Descripción', help_text='Descripción de la Provincia en Español.')
    descripcion_en = models.TextField(u'Descripción', help_text='Descripción de la Provincia en Inglés.')
    imagen = models.ImageField('Imagen', upload_to='provincia', help_text='Imagen de la Provincia.')
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
    descripcion_es = models.TextField(u'Descripción', help_text='Descripción del Municipio en Español.')
    descripcion_en = models.TextField(u'Descripción', help_text='Descripción del Municipio en Inglés.')
    imagen = models.ImageField('Imagen', upload_to='municipio', help_text='Imagen del Municipio.')
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
    descripcion_es = models.TextField(u'Descripción', help_text='Descripción de la Institución en Español.')
    descripcion_en = models.TextField(u'Descripción', help_text='Descripción de la Institución en Inglés.')
    imagen = models.ImageField('Imagen', upload_to='institucion', help_text='Imagen de la Institucion.')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='institucion')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='institucion')
    disponible = models.BooleanField(default=True)
    cant_images = property(lambda self: self.imagenes.count())

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class Imagenes(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='imagenes')
    nombre = models.CharField(max_length=32)
    descripcion_es = models.TextField(u'Descripción de la Imagen en Español.')
    descripcion_en = models.TextField(u'Descripción de la Imagen en Inglés.')
    photo = models.ImageField('Imagen', upload_to=photo_path, help_text='Imágenes del lugar.')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
