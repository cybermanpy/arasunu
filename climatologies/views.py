from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import FormSearch
from .models import Climatology

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