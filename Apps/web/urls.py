from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index),

    # Propietarios
    path('propietarios/', views.propietario_list, name='propietarios_list'),
    path('propietarios/crear/', views.propietario_create, name='propietario_create'),
    path('propietarios/editar/<int:pk>/', views.propietario_edit, name='propietario_edit'),
    path('propietarios/eliminar/<int:pk>/', views.propietario_delete, name='propietario_delete'),

    # Inmuebles
    path('inmuebles/', views.inmueble_list, name='inmuebles_list'),
    path('inmuebles/crear/', views.inmueble_create, name='inmueble_create'),
    path('inmuebles/editar/<int:pk>/', views.inmueble_edit, name='inmueble_edit'),
    path('inmuebles/eliminar/<int:pk>/', views.inmueble_delete, name='inmueble_delete'),

    # Reformas
    path('reformas/', views.reforma_list, name='reformas_list'),
    path('reformas/crear/', views.reforma_create, name='reforma_create'),
    path('reformas/editar/<int:pk>/', views.reforma_edit, name='reforma_edit'),
    path('reformas/eliminar/<int:pk>/', views.reforma_delete, name='reforma_delete'),

    # Cotizaciones
    path('cotizaciones/', views.cotizacion_list, name='cotizaciones_list'),
    path('cotizaciones/crear/', views.cotizacion_create, name='cotizacion_create'),
    path('cotizaciones/editar/<int:pk>/', views.cotizacion_edit, name='cotizacion_edit'),
    path('cotizaciones/eliminar/<int:pk>/', views.cotizacion_delete, name='cotizacion_delete'),

    # Control de Costos
    path('costos/', views.control_costo_list, name='control_costos_list'),
    path('costos/crear/', views.control_costo_create, name='control_costo_create'),
    path('costos/editar/<int:pk>/', views.control_costo_edit, name='control_costo_edit'),
    path('control_costos/eliminar/<int:pk>/', views.control_costo_delete, name='control_costo_delete'),
]
