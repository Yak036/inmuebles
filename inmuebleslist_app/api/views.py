from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET' , 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer =  InmuebleSerializer(inmuebles,many=True)
        
        return Response(serializer.data)

    if request.method == 'POST':
            de_serializer =  InmuebleSerializer(data=request.data)
            if de_serializer.is_valid():
                de_serializer.save()
            return Response(de_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    if request.method == 'GET':
        # buscar el inmueble mediante el id
        inmueble = Inmueble.objects.get(id=pk)
        # serializar el inmueble (mediante la funcion creada en el archivo serializers.py)
        serializer =  InmuebleSerializer(inmueble)
        # retornar dicho inmueble
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # buscar el inmueble mediante el id
        inmueble = Inmueble.objects.get(id=pk)
        # deserializar el inmueble para poder modificarlo y a la vez actualizarlo con la variable data
        de_serializer =  InmuebleSerializer(instance=inmueble,data=request.data)
        # validar la serializacion y actualizar datos
        if de_serializer.is_valid():
            de_serializer.save()
        return Response(de_serializer.data)
    
    if request.method == 'DELETE':
        inmueble = Inmueble.objects.get(id=pk)
        inmueble.delete()
        return Response("Inmueble Eliminado")
    
