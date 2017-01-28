from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from .models import Department
import json
from django.core import serializers

def DepartmentList(request):
    title = 'Arasunu'
    template = loader.get_template('department_list.html')
    object_list = Department.objects.all()
    context = {
        'title': title,
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))

def departmentJson(request, pk):
    c = get_object_or_404(Department, id=pk)
    data = {
        'id': c.id,
        'name': c.nombre_dpto,
    }
    jsonData = json.dumps(data)
    return HttpResponse(jsonData, content_type="application/json")

def listJson(request):
    departmentList = Department.objects.all()
    jsonData = serializers.serialize('json', departmentList)
    return HttpResponse(jsonData, content_type="application/json")