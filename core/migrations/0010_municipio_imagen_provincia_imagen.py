# Generated by Django 4.2.4 on 2023-08-27 17:34

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_municipio_descripcion_provincia_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='imagen',
            field=models.ImageField(default=1, help_text='Imagen del Municipio.', upload_to='', verbose_name='Imagen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provincia',
            name='imagen',
            field=models.ImageField(default=1, help_text='Imagen de la Provincia.', upload_to='', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
