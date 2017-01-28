from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^history/$', views.History, name='history'),
    # url(r'^', views.Weather, name='weather'),
]
