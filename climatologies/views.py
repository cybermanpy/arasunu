# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import FormSearch, FormGraphic
from .models import Climatology
import json
from django.http import JsonResponse
from django.core.serializers.json import Serializer

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
    object_list = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=2013).order_by('fecha')[:5]
    data = [{'data': item.tmax} for item in object_list]
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')

def ClimaJson2(request):
    object_list = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=2013).order_by('fecha')[:5]
    data = [{'Letter': item.tmax, 'Freq': item.tmin} for item in object_list]
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')

def Graphic(request):
    title = 'Arasunu'
    template = loader.get_template('graphic.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


# def climaParam(request):
#     year = request.GET.get('year', None)
#     text = request.GET.get('text', None)
#     data = {
#         'is_taken': Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains=text, fecha__year=year).exists()
#     }
#     return JsonResponse(data)

def climaParam(request):
    text = request.GET.get('text', None)
    month = request.GET.get('month', None)
    year = request.GET.get('year', None)
    object_list = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains=text, fecha__year=year, fecha__month=month).order_by('fecha')
    data = [{'Freq': item.tmin, 'Letter': item.tmax} for item in object_list]
    return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')

def getForm(request):
    title = 'Arasunu'
    form = FormGraphic()
    template = loader.get_template('formcopy.html')
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def getFormc3(request):
    title = 'Arasunu'
    template = loader.get_template('formc3.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

# def ClimaJson(request):
#     records = Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=2013).order_by('fecha')[:5]
#     json_res = []
#     for record in records:
#         json_obj = dict(
#             data = record.tmax,
#         )
#         json_res.append(json_obj)
#     return HttpResponse(json.dumps(json_res), content_type='application/json')

# def ClimaJson(request):
#     data = MySerializer().serialize(Climatology.objects.filter(id_estacion_id__id_ciudad__nombre__icontains='Luque', fecha__year=2013).order_by('fecha')[:5], fields=('tmax'))
#     return HttpResponse(data)
#     # return HttpResponse(json.dumps(data, ensure_ascii=False, encoding="utf-8"), content_type='application/json')

# class MySerializer(Serializer):
#     internal_use_only = False
#     def get_dump_object(self, obj):
#         data = super(MySerializer, self).get_dump_object(obj)
#         newdata = {}
#         newdata.update(data['fields'])
#         # newdata['pk'] = data['pk']
#         return newdata