from django.db import models
from pastores.enums import Distincion
# Create your models here.

class Iglesia(models.Model):
    class Meta:
        verbose_name = 'Iglesia'
        verbose_name_plural = 'Iglesias'

    pastor      = models.ForeignKey(
        'pastores.Persona', 
        on_delete=models.PROTECT, 
        null=True,
        limit_choices_to={'distincion': Distincion.PASTOR, 'esposa': None}
    )
    nombre      = models.CharField(max_length=100)
    email       = models.EmailField(unique=True, blank=True, null=True)
    direccion   = models.CharField(max_length=150, blank=True)
    ciudad      = models.ForeignKey(
        'paises.Ciudad', 
        on_delete=models.PROTECT
    )






