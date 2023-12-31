# Generated by Django 4.2.4 on 2023-08-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_municipio_imagen_provincia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='imagen',
            field=models.ImageField(help_text='Imagen del Municipio.', upload_to='municipio', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='imagen',
            field=models.ImageField(help_text='Imagen de la Provincia.', upload_to='provincia', verbose_name='Imagen'),
        ),
    ]
