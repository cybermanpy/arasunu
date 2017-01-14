# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from departments.models import Department

class City(models.Model):
    id_dpto = models.ForeignKey(Department, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.nombre)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ('id',)