from __future__ import unicode_literals

from django.db import models
from locations.models import Location

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=240, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.name, self.location.id)

    class Meta:
        verbose_name = 'Estacion'
        verbose_name_plural = 'Estaciones'
        ordering = ('id',)