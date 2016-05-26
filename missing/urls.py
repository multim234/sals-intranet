from .views import missing
from django.conf.urls import url

app_name = "missing"

urlpatterns = [
    url(r'^$', missing, name="missing")
        ]
