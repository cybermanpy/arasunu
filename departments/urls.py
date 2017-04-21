from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arasunu/departamento/lista/$', views.DepartmentList, name='lista'),
    url(r'^api/v2/(?P<pk>[0-9]+)/$', views.departmentJson, name='departmentJson' ),
    url(r'^api/v3/$', views.listJson, name='listJson' ),
]
