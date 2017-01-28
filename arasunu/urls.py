from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('departments.urls', namespace='departments')),
    url(r'^', include('climatologies.urls', namespace='climatologies')),
    url(r'^', include('locations.urls', namespace='locations')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
