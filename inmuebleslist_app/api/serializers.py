from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa


class EmpresaSerializer(serializers.Serializer):
    class Meta:
        model = Empresa
        fields = '__all__'



class EdificacionSerializer(serializers.ModelSerializer):
    # longitud_direccion = serializers.SerializerMethodField()
    
    class Meta:
        model = Edificacion
        # * mostrar todas las columnas
        fields = '__all__'
        # * mostrar solo estas columnas
        # fields = [
        #     'id',
        #     'pais',
        #     'imagen',
        #     'active',
        # ]
        # * excluir estas columnas
        # exclude = [
        #     'id'
        # ]
        
        
        
        # ? validaciones
    # def get_longitud_direccion(self, obj):
    #     return len(obj.direccion)
    
    # # * validate hace q sea global
    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError('La direccion y el pais no pueden ser iguales')
    #     return data
    
    # # * validate_imagen especifica que campo se validara
    # def validate_imagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError('La url de la immagen es demasiado corta')
    #     return data

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('El valor es demasiado corta')

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         # la instancia representa el objeto en la base de datos
#         # validated_data es lo que nos llega de la peticion
#         # compara ambas y actualiza las diferentes
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#     # * validate hace q sea global
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError('La direccion y el pais no pueden ser iguales')
#         return data
#     # * validate_imagen especifica que campo se validara
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError('La url de la immagen es demasiado corta')
#         return value