# Generated by Django 4.2.4 on 2023-09-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_rename_instimagenes_imagenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='phone',
            field=models.CharField(default=1, max_length=64, verbose_name='Teléfono'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
    ]