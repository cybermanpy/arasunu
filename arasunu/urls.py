from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from climatologies.views import Weather

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('departments.urls', namespace='departments')),
    url(r'^', include('climatologies.urls', namespace='climatologies')),
    url(r'^', include('locations.urls', namespace='locations')),
    url(r'^', include('hydrologies.urls', namespace='hydrologies')),
    url(r'^', Weather, name='weather'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
