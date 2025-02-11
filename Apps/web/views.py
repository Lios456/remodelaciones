from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Propietario, Inmueble, Reforma, Cotizacion, ControlCosto
from .forms import PropietarioForm, InmuebleForm, ReformaForm, CotizacionForm, ControlCostoForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
#Index

def index(request):
    context = {}
    
    return render(request, 'index.html', context)


# Propietarios Views

def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietarios/lista.html', {'propietarios': propietarios})

def propietario_create(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('propietarios_list')  # Redirige al listado de propietarios
    else:
        form = PropietarioForm()
    return render(request, 'propietarios/crear.html', {'form': form})

def propietario_edit(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = PropietarioForm(request.POST,request.FILES, instance=propietario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('propietarios_list')  # Redirige al listado de propietarios
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'propietarios/editar.html', {'form': form})

def propietario_delete(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        propietario.delete()
        messages.success(request, 'Propietario eliminado correctamente')
        return redirect('propietarios_list')
    return render(request, 'eliminar.html', {'objeto': propietario, 'url': 'propietarios_list'})

# Inmuebles Views

def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/lista.html', {'inmuebles': inmuebles})

def inmueble_create(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('inmuebles_list')  # Redirige al listado de inmuebles
    else:
        form = InmuebleForm()
    return render(request, 'inmuebles/crear.html', {'form': form})

def inmueble_edit(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('inmuebles_list')  # Redirige al listado de inmuebles
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'inmuebles/editar.html', {'form': form})

def inmueble_delete(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        inmueble.delete()
        messages.success(request, 'Inmueble eliminado correctamente')
        return redirect('inmuebles_list')
    return render(request, 'eliminar.html', {'objeto': inmueble, 'url': 'inmuebles_list'})
# Reformas Views

def reforma_list(request):
    reformas = Reforma.objects.all()
    return render(request, 'reformas/lista.html', {'reformas': reformas})

def reforma_create(request):
    if request.method == 'POST':
        form = ReformaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('reformas_list')  # Redirige al listado de reformas
    else:
        form = ReformaForm()
    return render(request, 'reformas/crear.html', {'form': form})

def reforma_edit(request, pk):
    reforma = get_object_or_404(Reforma, pk=pk)
    if request.method == 'POST':
        form = ReformaForm(request.POST, instance=reforma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('reformas_list')  # Redirige al listado de reformas
    else:
        form = ReformaForm(instance=reforma)
    return render(request, 'reformas/editar.html', {'form': form})

def reforma_delete(request, pk):
    reforma = get_object_or_404(Reforma, pk=pk)
    if request.method == 'POST':
        reforma.delete()
        messages.success(request, 'Reforma eliminada correctamente')
        return redirect('reformas_list')
    return render(request, 'eliminar.html', {'objeto': reforma, 'url': 'reformas_list'})
# Cotizaciones Views

def cotizacion_list(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'cotizaciones/lista.html', {'cotizaciones': cotizaciones})

def cotizacion_create(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            cotizacion = form.save()
            reforma = cotizacion.reforma
            inmueble = reforma.inmueble
            propietario = inmueble.propietario
            
            """
            Mandar el correo al guardar la cotización
            """
            subject = 'Propuesta de cotización'
            message = f"""
                Fecha de emisión: {cotizacion.fecha_emision}
                ___________________________________________________________________________________
                
                Hola {propietario.nombre}. Tenemos una cotización de {cotizacion.proveedor} para ti.+
                
                
                Detalles de la cotización:
                Costo estimado: {cotizacion.costo_estimado}
                Descripción: {cotizacion.descripcion}
                Fecha de vencimiento: {cotizacion.fecha_vencimiento}
                ___________________________________________________________________________________
                
                Detalles de tu reforma:
                Descripción: {reforma.descripcion}
                Fecha de inicio: {reforma.fecha_inicio}
                Estado: {reforma.estado}
                ___________________________________________________________________________________

                Detalles de tu inmueble
                Dirección: {inmueble.direccion} 
                Tipo: {inmueble.tipo}
                Descripción: {inmueble.descripcion}
                    
                ___________________________________________________________________________________
                
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [propietario.correo]

            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Registro correcto')
            return redirect('cotizaciones_list')  # Redirige al listado de cotizaciones
    else:
        form = CotizacionForm()
    return render(request, 'cotizaciones/crear.html', {'form': form})

def cotizacion_edit(request, pk):
    cotizacion = get_object_or_404(Cotizacion, pk=pk)
    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance=cotizacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('cotizaciones_list')  # Redirige al listado de cotizaciones
    else:
        form = CotizacionForm(instance=cotizacion)
    return render(request, 'cotizaciones/editar.html', {'form': form})

def cotizacion_delete(request, pk):
    cotizacion = get_object_or_404(Cotizacion, pk=pk)
    if request.method == 'POST':
        cotizacion.delete()
        messages.success(request, 'Cotización eliminada correctamente')
        return redirect('cotizaciones_list')
    return render(request, 'eliminar.html', {'objeto': cotizacion, 'url': 'cotizaciones_list'})
# Control de Costos Views

def control_costo_list(request):
    costos = ControlCosto.objects.all()
    return render(request, 'control_costos/lista.html', {'costos': costos})

def control_costo_create(request):
    if request.method == 'POST':
        form = ControlCostoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('control_costos_list')  # Redirige al listado de costos
    else:
        form = ControlCostoForm()
    return render(request, 'control_costos/crear.html', {'form': form})

def control_costo_edit(request, pk):
    costo = get_object_or_404(ControlCosto, pk=pk)
    if request.method == 'POST':
        form = ControlCostoForm(request.POST, request.FILES, instance=costo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro correcto')
            return redirect('control_costos_list')  # Redirige al listado de costos
    else:
        form = ControlCostoForm(instance=costo)
    return render(request, 'control_costos/editar.html', {'form': form})

def control_costo_delete(request, pk):
    costo = get_object_or_404(ControlCosto, pk=pk)
    if request.method == 'POST':
        costo.delete()
        messages.success(request, 'Control de costo eliminado correctamente')
        return redirect('control_costos_list')
    return render(request, 'eliminar.html', {'objeto': costo, 'url': 'control_costos_list'})