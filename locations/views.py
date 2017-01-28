from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from .models import Location
from django.shortcuts import get_object_or_404
import json

def locationJson(request, pk):
    c = get_object_or_404(Location, id=pk)
    data = {
        'id': c.id,
        'lon_seg': c.lon_seg,
    }
    jsonData = json.dumps(data)
    return HttpResponse(jsonData, content_type="application/json")


def listLocationJson(request):
    get_list = Location.objects.all()
    jsonData = serializers.serialize('json', get_list)
    return HttpResponse(jsonData, content_type="application/json")

def getLocation(request):
    # queryset = Location.objects.all()[:3]
    # data = [{'lat': str(item.lat_gra), 'lng': str(item.lon_dec)} for item in queryset]
    data = [
        { 
            "lat": 57.95, 
            "lng": 14.65, 
            "content":"test content1" 
        }, 
        { 
            "lat": 57.9, 
            "lng": 14.6, 
            "content":"test content2" 
        }, 
        { 
            "lat": 57.85, 
            "lng": 14.55,
            "content":"test content3"
        }
    ]
    return HttpResponse(json.dumps(data), content_type='application/json')

def viewMap(request):
    template = loader.get_template('maps3.html')
    context = {
    }
    return HttpResponse(template.render(context, request))