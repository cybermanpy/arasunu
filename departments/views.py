from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Department

def DepartmentList(request):
    title = 'Arasunu'
    template = loader.get_template('department_list.html')
    object_list = Department.objects.all()
    context = {
        'title': title,
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))