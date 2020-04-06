from django.contrib import admin
from .models import Persona, Matrimonio, Telefono

# Register your models here.

# class TelefonoInline(admin.TabularInline):
#     model = Telefono
#     max_num = 4


# class PersonaAdmin(admin.ModelAdmin):
#     #create, update
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'nombre', 
#                 'email',
#                 'ciudad',
#                 'distincion',
#                 ('paternidad', 'paternidad_fecha',),
#                 ),
#         }),
#         ('Baja', {
#             'classes': ('collapse',),
#             'fields': ('baja_motivo', 'baja_fecha',),
#         }),
#     )
#     readonly_fields = ('baja_fecha', 'paternidad_fecha',)
#     autocomplete_fields = ['ciudad']
#     inlines = [
#         TelefonoInline,
#     ]

#     #list
#     list_display_links = ('nombre',)
#     list_display = ('id', 'nombre', 'get_telefonos', 'email', 'ciudad', 'get_provincia', 'get_pais')
    
#     def get_provincia(self, obj):
#         return obj.ciudad.provincia
#     get_provincia.short_description = 'Provincia'
#     get_provincia.admin_order_field = 'ciudad__provincia'
    
#     def get_pais(self, obj):
#         return obj.ciudad.provincia.pais
#     get_pais.short_description = 'País'
#     get_pais.admin_order_field = 'ciudad__provincia__pais'

#     def get_telefonos(self, obj):
#         return list(obj.telefonos.all())
#     get_telefonos.short_description = 'Telefonos'
    

admin.site.register(Persona)
admin.site.register(Telefono)
admin.site.register(Matrimonio)