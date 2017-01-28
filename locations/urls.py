from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/(?P<pk>[0-9]+)/$', views.locationJson, name='locationJson' ),
    url(r'^api/v4/$', views.listLocationJson, name='listLocationJson' ),
    url(r'^api/v5/$', views.getLocation, name='getLocation' ),
    url(r'^maps/$', views.viewMap, name='viewMap' ),
]