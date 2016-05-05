from django.conf.urls import url
from planning_modifications.views import *

app_name = "planning_modification"

urlpatterns = [
    url(r'^$', modifications, name="modifications")
]
