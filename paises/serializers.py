from .models import Pais, Provincia
from rest_framework import serializers

class PaisSerializer(serializers.HyperlinkedModelSerializer):
    provincias = serializers.HyperlinkedRelatedField(many=True, view_name='provincia-detail', read_only=True)
    
    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'provincias',]

class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'pais', 'nombre',]