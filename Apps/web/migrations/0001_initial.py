# Generated by Django 5.1.5 on 2025-02-06 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Oficina', 'Oficina')], max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_adquisicion', models.DateField()),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=50)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inmuebles', to='web.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Reforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_terminacion', models.DateField(blank=True, null=True)),
                ('costo_estimado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo_real', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(choices=[('En Proceso', 'En Proceso'), ('Finalizada', 'Finalizada'), ('Pendiente', 'Pendiente')], max_length=50)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reformas', to='web.inmueble')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=255)),
                ('costo_estimado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('reforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizaciones', to='web.reforma')),
            ],
        ),
        migrations.CreateModel(
            name='ControlCosto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('reforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costos', to='web.reforma')),
            ],
        ),
    ]
