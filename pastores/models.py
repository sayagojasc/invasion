from django.db import models
from .enums import Paternidad, Distincion, BajaMotivo, TipoTelefono
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

# Create your models here.

class Persona(models.Model):
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    nombre              = models.CharField(max_length=100)
    email               = models.EmailField(unique=True, blank=True)
    paternidad          = models.IntegerField(
        choices=Paternidad.choices,
        default=Paternidad.NO
    )
    paternidad_fecha    = models.DateField(null=True, default=None, blank=True, verbose_name='Fecha')
    ciudad              = models.ForeignKey('paises.Ciudad', on_delete=models.PROTECT)
    distincion          = models.IntegerField(
        choices=Distincion.choices,
        default=Distincion.NO_INFORMADO
    )
    baja_fecha          = models.DateTimeField(null=True, default=None, blank=True, verbose_name='Fecha')
    baja_motivo         = models.IntegerField(
        choices=BajaMotivo.choices,
        default=BajaMotivo.NO,
        verbose_name='Motivo'
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.baja_motivo != BajaMotivo.NO:
            import datetime
            self.baja_fecha = datetime.datetime.now()
        else:
            self.baja_fecha = None

        if self.paternidad != Paternidad.NO:
            import datetime
            self.paternidad_fecha = datetime.datetime.now()
        else:
            self.paternidad_fecha = None
        super(Persona, self).save(*args, **kwargs)

class Matrimonio(models.Model):
    esposo = models.OneToOneField('pastores.Persona', on_delete=models.CASCADE, related_name='esposo', related_query_name='esposo')
    esposa = models.OneToOneField('pastores.Persona', on_delete=models.CASCADE, related_name='esposa', related_query_name='esposa')

class Telefono(models.Model):
    persona     = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='telefonos',
        related_query_name='telefono',)
    numero      = PhoneNumberField(unique=True)
    tipo        = models.IntegerField(
        choices=TipoTelefono.choices,
        default=TipoTelefono.MOVIL
    )
    whatsapp    = models.BooleanField(default=False)

    def __str__(self):
        return str(self.numero)


