from django.contrib import admin
from .models import Pais, Provincia, Ciudad

# Register your models here.

# class CiudadAdmin(admin.ModelAdmin):
#     search_fields = ['nombre']

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)