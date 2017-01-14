from django.contrib import admin
from .models import Location

@admin.register(Location)
class AdminLocation(admin.ModelAdmin):
    list_display = ('id', 'id_ciudad', 'lon_gra',)
