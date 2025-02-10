from django.db import models

# Modelo para los propietarios
class Propietario(models.Model):
    dni = models.CharField(max_length=10, verbose_name='DOCUMENTO DE IDENTIFICACIÓN', unique=True, null=True)
    foto = models.ImageField(verbose_name='FOTO DEL PROPIETARIO:', upload_to='propietarios/', null=True)
    nombre = models.CharField(max_length=255, verbose_name='NOMBRE:')
    correo = models.EmailField(verbose_name='CORREO:')
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name='TELÉFONO')
    direccion = models.CharField(max_length=255, null=True, blank=True, verbose_name='DIRECCIÓN')

    def __str__(self):
        return self.nombre

# Modelo para los inmuebles
class Inmueble(models.Model):
    direccion = models.CharField(max_length=255, verbose_name='DIRECCIÓN')
    foto = models.ImageField(verbose_name='FOTO DEL INMUEBLE:', upload_to='inmuebles/', null=True)
    tipo = models.CharField(max_length=100, choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Oficina', 'Oficina')], verbose_name='TIPO')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='inmuebles', verbose_name='PROPIETARIO')
    descripcion = models.TextField(null=True, blank=True, verbose_name='DESCRIPCIÓN')
    fecha_adquisicion = models.DateField(verbose_name='FECHA DE ADQUISICIÓN')
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], verbose_name='ESTADO')

    def __str__(self):
        return f'{self.tipo} en {self.direccion}'

# Modelo para las reformas
class Reforma(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='reformas', verbose_name='INMUEBLE DE LA REFORMA')
    descripcion = models.TextField(verbose_name='ACCIONES A REALIZAR')
    fecha_inicio = models.DateField(verbose_name='FECHA DE INICIO')
    fecha_terminacion = models.DateField(null=True, blank=True, verbose_name='FECHA DE FIN (DEJAR EN BLANCO SI NO SE HA FINALIZADO)')
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='COSTO ESTIMADO')
    costo_real = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='COSTO REAL (DEJAR EN BLANCO SI AÚN NO SE TERMINA LA REFORMA)')
    estado = models.CharField(max_length=50, choices=[('En Proceso', 'En Proceso'), ('Finalizada', 'Finalizada'), ('Pendiente', 'Pendiente')], verbose_name='ESTADO DE LA REFORMA')

    def __str__(self):
        return f'Reforma en {self.inmueble}'

# Modelo para las cotizaciones
class Cotizacion(models.Model):
    reforma = models.ForeignKey(Reforma, on_delete=models.CASCADE, related_name='cotizaciones', verbose_name='REFORMA DE LA COTIZACIÓN')
    proveedor = models.CharField(max_length=255, verbose_name='PROVEEDOR')
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='COSTO ESTIMADO')
    descripcion = models.TextField(verbose_name='DESCRIPCIÓN DE LA COTIZACIÓN')
    fecha_emision = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(verbose_name='FECHA DE VENCIMIENTO')

    def __str__(self):
        return f'Cotización de {self.proveedor} para {self.reforma}'

# Modelo para el control de costos
class ControlCosto(models.Model):
    reforma = models.ForeignKey(Reforma, on_delete=models.CASCADE, related_name='costos', verbose_name='FEROMAR DEL COSTO')
    descripcion = models.CharField(max_length=255, verbose_name='DESCRIPCIÓN DEL COSTO')
    foto = models.ImageField(verbose_name='EVIDENCIA:', upload_to='costos/', null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='VALOR DE LA COTIZACIÓN')
    fecha = models.DateField(verbose_name='FECHA DEL COSTO')

    def __str__(self):
        return f'Costo de {self.descripcion} para la reforma {self.reforma}'
