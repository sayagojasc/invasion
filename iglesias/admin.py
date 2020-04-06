from django.contrib import admin
from .models import Iglesia
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

# Register your models here.

# class IglesiaAdmin(admin.ModelAdmin):
#     fields = ['pastor', 'nombre', 'email', 'direccion', 'ciudad']
#     list_display = ['nombre', 'pastor_link', 'ciudad', 'get_provincia', 'get_pais', 'pastor',]
#     list_editable = ['pastor',]

#     def pastor_link(self, obj):
#         content_type = ContentType.objects.get_for_model(obj.pastor.__class__)
#         return format_html('<a href={}><b>{}</b></a>', reverse(f'admin:{content_type.app_label}_{content_type.model}_change', args=(obj.pastor.id,)), obj.pastor)
#     pastor_link.short_description = 'Pastor'

#     def get_provincia(self, obj):
#         return obj.ciudad.provincia
#     get_provincia.short_description = 'Provincia'
#     get_provincia.admin_order_field = 'ciudad__provincia'
    
#     def get_pais(self, obj):
#         return obj.ciudad.provincia.pais
#     get_pais.short_description = 'País'
#     get_pais.admin_order_field = 'ciudad__provincia__pais'

    

admin.site.register(Iglesia)