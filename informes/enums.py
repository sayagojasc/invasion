from django.db import models

class Respuesta(models.IntegerChoices):
    NO_INFORMADO    = (0, 'No Informado')
    SI              = (1, 'Si')
    NO              = (2, 'No')
    DUDA            = (3, 'Duda')