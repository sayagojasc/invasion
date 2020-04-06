from django.shortcuts import render
from .models import Pais, Provincia
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PaisSerializer, ProvinciaSerializer

# Create your views here.

class PaisViewSet(viewsets.ModelViewSet):
    queryset =  Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [permissions.IsAuthenticated,]

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset =  Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [permissions.IsAuthenticated,]
