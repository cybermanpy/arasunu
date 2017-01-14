# coding=utf-8

from __future__ import unicode_literals

from django.db import models

class StationType(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.nombre)

    class Meta:
        verbose_name = 'Tipo Estación'
        verbose_name_plural = 'Tipos de Estaciones'
        ordering = ('id',)