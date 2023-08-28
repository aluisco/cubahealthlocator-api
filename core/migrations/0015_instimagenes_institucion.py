# Generated by Django 4.2.4 on 2023-08-27 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_instimagenes_core_instim_content_2c3ac1_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='instimagenes',
            name='institucion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='core.institucion'),
            preserve_default=False,
        ),
    ]
