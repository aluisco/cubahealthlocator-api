# Generated by Django 4.2.4 on 2023-08-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_instimagenes_core_instim_content_2c3ac1_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='imagen',
            field=models.ImageField(default=1, help_text='Imagen de la Institucion.', upload_to='institucion', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]