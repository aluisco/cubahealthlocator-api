# Generated by Django 4.2.4 on 2023-08-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_institucion_descripcion'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='instimagenes',
            index=models.Index(fields=['content_type', 'object_id'], name='core_instim_content_2c3ac1_idx'),
        ),
    ]