from django.db import models
from .enums import Respuesta
import datetime

# Create your models here.

def periodos():
    return [(r, str(r)) for r in range(2015, datetime.date.today().year+2)]

def periodo_actual():
    return datetime.date.today().year

PERIODOS = periodos()

class InformeAbstracto(models.Model):

    class Meta:
        abstract = True

    iglesia     = models.ForeignKey('iglesias.Iglesia', on_delete=models.PROTECT)
    periodo     = models.IntegerField(choices=PERIODOS, default=periodo_actual)
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