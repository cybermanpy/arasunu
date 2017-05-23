# coding=utf-8

from django import forms
from hydrologies.models import Hydrology
from stationtypes.models import StationType
from cities.models import City
from datetime import datetime

class FormHydrology(forms.Form):
    n = tuple((str(n), str(n)) for n in range(1973, datetime.now().year + 1))
    object_list = StationType.objects.all()
    text = forms.ChoiceField(choices=((x.nombre, x.nombre) for x in object_list ), error_messages={'required': 'Este campo es obligatorio'})
    fecha = forms.ChoiceField(choices=n, error_messages={'required': 'Este campo es obligatorio'})
    city_list = City.objects.all().order_by('nombre')
    city = forms.ChoiceField(choices=((x.nombre, x.nombre) for x in city_list ), error_messages={'required': 'Este campo es obligatorio'})
