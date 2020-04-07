from django.db import models

# Create your models here.

class Pais(models.Model):
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['pais__nombre']
        
    pais    = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='provincias')
    nombre  = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

class Ciudad(models.Model):
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['provincia']
        unique_together = ['nombre', 'provincia',]
        
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, related_name='provincias')
    nombre  = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'
    