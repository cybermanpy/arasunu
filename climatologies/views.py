# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import FormSearch, FormGraphic
from .models import Climatology
import json
from django.http import JsonResponse

def History(request):
    title = 'Arasunu'
    text = 'Busqueda de historicos de temperatura'
    template = loader.get_template('history.html')
    if request.method == 'POST':
        form = FormSearch(request.POST)
        search = request.POST['text']
        fecha = request.POST['fecha']
        if form.is_valid():
            object_list = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains=search, fecha__year=fecha).order_by('-fecha')
            context = {
                'title': title,
                'text': text,
                'form': form,
                'object_list': object_list,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    context = {
        'title': title,
        'text': text,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def Weather(request):
    title = 'Arasunu'
    template = loader.get_template('weather.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

def ClimaJson(request):
    object_list = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=2013).order_by('fecha')
    data = [{'Estación': item.nombre_estacion, 'Temp': int(item.vmax_d), 'Fecha':str(item.fecha)} for item in object_list ]
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')

def Graphic(request):
    title = 'Arasunu'
    template = loader.get_template('graphic.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def climaParam(request):
    year = request.GET.get('year', None)
    # text = request.GET.get('text', None)
    data = {
        'is_taken': Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=year).exists()
    }
    return JsonResponse(data)

def getForm(request):
    title = 'Arasunu'
    form = FormGraphic()
    template = loader.get_template('form.html')
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))