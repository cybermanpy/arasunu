from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^api/v4/json/(?P<city>[\w]+)/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.HydroJson, name='HydroJson'),
        url(r'^hydrology/form/$', views.getFormHydro, name='getFormHydro'),
        url(r'^hydrology/ajax/$', views.climaParam1, name='climaParam1'),
        url(r'^hydrology/maps/$', views.viewMap, name='viewMap'),
        url(r'^hydrology/stations/$', views.viewStation, name='viewStation'),
        url(r'^hydrology/stations/auto/$', views.viewStationAuto, name='viewStationAuto'),
]