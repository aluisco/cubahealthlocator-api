# Generated by Django 4.2.4 on 2023-08-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_instimagenes_institucion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]