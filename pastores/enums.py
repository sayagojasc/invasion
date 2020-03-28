from django.db import models

class Paternidad(models.IntegerChoices):
    NO          = (0, 'No')
    HIJO        = (1, 'Hijo')
    ADMISION    = (2, 'Proceso Admisión')

class Distincion(models.IntegerChoices):
    NO_INFORMADO    = (0, 'No Informado')
    PASTOR          = (1, 'Pastor Principal')
    PASTOR_ADJUNTO  = (2, 'Pastor Adjunto')
    SECRETARIO      = (3, 'Secretario')
    LIDER           = (4, 'Líder')
    MIEMBRO         = (5, 'Miembro')

class BajaMotivo(models.IntegerChoices):
    NO          = (0, 'No')
    SIN_INTERES = (1, 'Sin Interés')
    FALLECIO    = (2, 'Falleció')
    ERA_PASTOR  = (3, 'Ya no es pastor')

class TipoTelefono(models.IntegerChoices):
    MOVIL   = (1, 'Móvil')
    CASA    = (2, 'Casa')
    TRABAJO = (3, 'Trabajo')
