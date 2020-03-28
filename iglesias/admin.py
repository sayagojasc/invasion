from django.contrib import admin
from .models import Iglesia

# Register your models here.

class IglesiaAdmin(admin.ModelAdmin):
    fields = ['pastor', 'nombre', 'email', 'direccion', 'ciudad']
    list_display = ['nombre', 'pastor', 'ciudad', 'get_provincia', 'get_pais']

    def get_provincia(self, obj):
        return obj.ciudad.provincia
    get_provincia.short_description = 'Provincia'
    get_provincia.admin_order_field = 'ciudad__provincia'
    
    def get_pais(self, obj):
        return obj.ciudad.provincia.pais
    get_pais.short_description = 'País'
    get_pais.admin_order_field = 'ciudad__provincia__pais'

    

admin.site.register(Iglesia, IglesiaAdmin)