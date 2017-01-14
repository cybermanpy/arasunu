# coding=utf-8

from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
    nombre_dpto = models.CharField(max_length=100, blank=False, null=False)
    nombre_cap = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.nombre_dpto)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('id',)
