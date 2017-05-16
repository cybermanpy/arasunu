from django.contrib import admin
from .models import Hydrology

@admin.register(Hydrology)
class AdminHydrology(admin.ModelAdmin):
    list_display = ('id', 'station', 'nombre_estacion',  'max', 'min')
    list_filter = ('station', )