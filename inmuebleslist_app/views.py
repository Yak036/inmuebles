from django.shortcuts import render
from inmuebleslist_app.models import Inmueble
from django.http import JsonResponse
# Create your views here.

def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles': list(inmuebles.values())
    }
    
    return JsonResponse(data)

def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk=pk)
    data = {
        'inmueble': {
            'id': inmueble.id,
            'direccion': inmueble.direccion,
            'pais': inmueble.pais,
            'descripcion': inmueble.descripcion,
            'imagen': inmueble.imagen,
            'active': inmueble.active
        }
    }
    return JsonResponse(data)