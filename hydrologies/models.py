# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from locations.models import Location
from stationtypes.models import StationType
from stations.models import Station

class Hydrology(models.Model):
    id_estacion = models.ForeignKey(Location, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(StationType, on_delete=models.CASCADE)
    nombre_estacion = models.CharField(max_length=60, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    altura = models.CharField(max_length=10, blank=True, null=True)
    max = models.CharField(max_length=10, blank=True, null=True)
    med = models.CharField(max_length=10, blank=True, null=True)
    min = models.CharField(max_length=10, blank=True, null=True)
    p10 = models.CharField(max_length=10, blank=True, null=True)
    p50 = models.CharField(max_length=10, blank=True, null=True)
    p90 = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.nombre_estacion)

    class Meta:
        verbose_name = 'Hidrología'
        verbose_name_plural = 'Hidrologias'