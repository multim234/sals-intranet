from django.conf.urls import url
from .views import *

app_name = "self_menu"
urlpatterns = [
    url(regex=r'^$', view=self_menu, name='self_menu'),
]
