from django.conf.urls import url
from planning_modifications.views import *

app_name = "planning_modifications"

urlpatterns = [
    url(r'^$', modifications, name="modifications")
]
