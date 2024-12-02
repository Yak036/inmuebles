from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)