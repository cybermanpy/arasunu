from django.contrib import admin
from .models import Climatology

@admin.register(Climatology)
class AdminClimatology(admin.ModelAdmin):
    list_display = ('id', 'station', 'nombre_estacion',  'tmax', 'tmin')
    list_filter = ('station', )