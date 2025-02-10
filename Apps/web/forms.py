from django import forms
from .models import Propietario, Inmueble, Reforma, Cotizacion, ControlCosto

# Formulario para Propietarios
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['dni','foto','nombre', 'correo', 'telefono', 'direccion']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control file-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulario para Inmuebles
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['direccion','foto','tipo', 'propietario', 'descripcion', 'fecha_adquisicion', 'estado']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control file-input'}),
            'tipo': forms.Select(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Oficina', 'Oficina')], attrs={'class': 'form-control select2'}),
            'propietario': forms.Select(attrs={'class': 'form-control select2'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado': forms.Select(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], attrs={'class': 'form-control'}),
        }

# Formulario para Reformas
class ReformaForm(forms.ModelForm):
    class Meta:
        model = Reforma
        fields = ['inmueble', 'descripcion', 'fecha_inicio', 'fecha_terminacion', 'costo_estimado', 'costo_real', 'estado']
        widgets = {
            'inmueble': forms.Select(attrs={'class': 'form-control select2'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_terminacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'costo_estimado': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_real': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(choices=[('En Proceso', 'En Proceso'), ('Finalizada', 'Finalizada'), ('Pendiente', 'Pendiente')], attrs={'class': 'form-control select2'}),
        }

# Formulario para Cotizaciones
class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['reforma', 'proveedor', 'costo_estimado', 'descripcion', 'fecha_vencimiento']
        widgets = {
            'reforma': forms.Select(attrs={'class': 'form-control select2'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_estimado': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# Formulario para Control de Costos
class ControlCostoForm(forms.ModelForm):
    class Meta:
        model = ControlCosto
        fields = ['reforma','foto', 'descripcion', 'monto', 'fecha']
        widgets = {
            'reforma': forms.Select(attrs={'class': 'form-control select2'}),
            'foto': forms.FileInput(attrs={'class': 'form-control file-input'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
