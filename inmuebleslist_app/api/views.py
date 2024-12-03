from inmuebleslist_app.models import Edificacion, Empresa
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# * separar los metodos en clases para hacerlo mas mantenible
class EmpresaListAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer =  EmpresaSerializer(empresas,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        de_serializer =  EmpresaSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionListAV(APIView):
    def get(self, request):
        edificaciones = Edificacion.objects.all()
        serializer =  EdificacionSerializer(edificaciones,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        de_serializer =  EdificacionSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EdificacionDetalleAV(APIView):
    # ? buscar 1 inmueble
    def get(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(id=pk)
            serializer =  EdificacionSerializer(edificacion)
            return Response(serializer.data)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Edificacion no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    # ? actualizar 1 inmueble
    def put(self, request, pk):
        edificacion = Edificacion.objects.get(id=pk)
        de_serializer =  EdificacionSerializer(instance=edificacion,data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ? eliminar 1 inmueble
    def delete(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(id=pk)
            edificacion.delete()
            return Response("Edificacion Eliminado", status=status.HTTP_204_NO_CONTENT)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Edificacion no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
    
    
# @api_view(['GET' , 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer =  InmuebleSerializer(inmuebles,many=True)
        
#         return Response(serializer.data)

#     if request.method == 'POST':
#             de_serializer =  InmuebleSerializer(data=request.data)
#             if de_serializer.is_valid():
#                 de_serializer.save()
#             return Response(de_serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             # buscar el inmueble mediante el id
#             inmueble = Inmueble.objects.get(id=pk)
#             # serializar el inmueble (mediante la funcion creada en el archivo serializers.py)
#             serializer =  InmuebleSerializer(inmueble)
#             # retornar dicho inmueble
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         # buscar el inmueble mediante el id
#         inmueble = Inmueble.objects.get(id=pk)
#         # deserializar el inmueble para poder modificarlo y a la vez actualizarlo con la variable data
#         # ? se debe crear el metodo update en el serializers.py
#         de_serializer =  InmuebleSerializer(instance=inmueble,data=request.data)
#         # validar la serializacion y actualizar datos
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(id=pk)
#             inmueble.delete()
#             return Response("Inmueble Eliminado", status=status.HTTP_204_NO_CONTENT)
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
