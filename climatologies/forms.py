from django import forms
from cities.models import City
from datetime import datetime

class FormSearch(forms.Form):
    n = tuple((str(n), str(n)) for n in range(1973, datetime.now().year + 1))
    city_list = City.objects.all().order_by('nombre')
    text = forms.ChoiceField(choices=((x.nombre, x.nombre) for x in city_list ), error_messages={'required': 'Este campo es obligatorio'})
    fecha = forms.ChoiceField(choices=n, error_messages={'required': 'Este campo es obligatorio'})

class FormGraphic(forms.Form):
    city_list = City.objects.all().order_by('nombre')
    c = ((x.nombre, x.nombre) for x in city_list )
    c = tuple([(u'', '------')] + list(c))
    text = forms.ChoiceField(choices=c, error_messages={'required': 'Este campo es obligatorio'})
    n = tuple((str(n), str(n)) for n in range(1973, datetime.now().year + 1))
    months = [('1','Enero'),
                  ('2','Febrero'),
                  ('3','Marzo'),
                  ('4','Abril'),
                  ('5','Mayo'),
                  ('6','Junio'),
                  ('7','Julio'),
                  ('8','Agosto'),
                  ('9','Setiembre'),
                  ('10','Octubre'),
                  ('11','Noviembre'),
                  ('12','Diciembre'),]
    months = tuple([(u'', '------')] + list(months))
    month = forms.ChoiceField(choices=months, error_messages={'required': 'Este campo es obligatorio'})
    n = tuple([(u'', '------')] + list(n))
    year = forms.ChoiceField(choices=n, error_messages={'required': 'Este campo es obligatorio'})