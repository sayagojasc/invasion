from .models import Pais, Provincia
from rest_framework import serializers

class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre',]

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'pais', 'nombre',]