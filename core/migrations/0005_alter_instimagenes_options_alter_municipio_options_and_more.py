# Generated by Django 4.2.4 on 2023-08-20 21:36

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_instimagenes_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instimagenes',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'ordering': ['nombre'], 'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AddField(
            model_name='institucion',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='provincia', to='core.provincia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instimagenes',
            name='descripcion',
            field=models.TextField(help_text='Descripción de la Imagen.', verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='instimagenes',
            name='photo',
            field=models.ImageField(help_text='Imágenes del lugar.', upload_to='', verbose_name='Imagen'),
        ),
    ]
