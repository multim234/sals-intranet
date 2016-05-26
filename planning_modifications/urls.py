from django.conf.urls import url
from .views import modifications

app_name = "planning_modifications"

urlpatterns = [
    url(r'^$', modifications, name="modifications")
]
