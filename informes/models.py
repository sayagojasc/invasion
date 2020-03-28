from django.db import models
from .enums import Respuesta
import datetime

# Create your models here.

def year_choices():
    return [(r, str(r)) for r in range(2015, datetime.date.today().year+2)]

def current_year():
    return datetime.date.today().year

YEAR_CHOICES = year_choices()

class InformeAbstracto(models.Model):

    class Meta:
        abstract = True

    iglesia     = models.ForeignKey('iglesias.Iglesia', on_delete=models.PROTECT)
    periodo     = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    respuesta   = models.IntegerField(choices=Respuesta.choices, default=Respuesta.NO_INFORMADO)
    observacion = models.TextField(blank=True)

class Invasion(InformeAbstracto):
    pass

class Convencion(InformeAbstracto):
    pass

class EscuelaSobrenatural(InformeAbstracto):
    pass

class Entrenamiento(InformeAbstracto):
    pass

class Comando(InformeAbstracto):
    pass