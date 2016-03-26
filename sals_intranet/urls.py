from django.conf.urls import url, include
from django.contrib import admin
from base import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('base.urls')),
    url(r'^absences/', include('missing.urls'))
]
