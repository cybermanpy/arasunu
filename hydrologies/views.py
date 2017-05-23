# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from climatologies.forms import FormSearch, FormGraphic
from .models import Hydrology
import json
from django.http import JsonResponse
from django.core.serializers.json import Serializer



def getFormHydro(request):
    title = 'Arasunu'
    form = FormGraphic() 
    template = loader.get_template('formhydro.html')
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def climaParam1(request):
    text = request.GET.get('text', None)
    month = request.GET.get('month', None)
    year = request.GET.get('year', None)
    data = {
        'city': text,
        'month': month,
        'year': year
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')


def HydroJson(request, city, month, year):
    object_list = Hydrology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains=city, fecha__month=month,  fecha__year=year).order_by('fecha')
    data = [{'Letter': int(item.fecha.day), 'Freq': item.max} for item in object_list]
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')
