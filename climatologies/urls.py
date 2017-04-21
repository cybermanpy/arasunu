from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^history/$', views.History, name='history'),
    url(r'^api/v1/json/$', views.ClimaJson, name='climaJson'),
    url(r'^graphic/$', views.Graphic, name='graphic'),
    url(r'^graphic/form/$', views.getForm, name='getForm'),
    url(r'^ajax/year/$', views.climaParam, name='climaParam'),
    url(r'^', views.Weather, name='weather'),
]
