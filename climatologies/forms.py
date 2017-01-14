from django import forms
from cities.models import City
from datetime import datetime

class FormSearch(forms.Form):
    n = tuple((str(n), str(n)) for n in range(1973, datetime.now().year + 1))
    city_list = City.objects.all().order_by('nombre')
    text = forms.ChoiceField(choices=((x.nombre, x.nombre) for x in city_list ), error_messages={'required': 'Este campo es obligatorio'})
    fecha = forms.ChoiceField(choices=n, error_messages={'required': 'Este campo es obligatorio'})
