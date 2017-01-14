from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arasunu/departamento/lista/$', views.DepartmentList, name='lista'),
]