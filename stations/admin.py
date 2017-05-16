from django.contrib import admin
from .models import Station

@admin.register(Station)
class AdminStation(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    list_filter = ('location', )