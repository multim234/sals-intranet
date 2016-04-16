from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('base.urls')),
    url(r'^absences/', include('missing.urls')),
    url(r'^modifications/', include('planning_modifications.urls')),
]
