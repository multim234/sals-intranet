from django.conf.urls import url 
from base.views import *

app_name = "base"
urlpatterns = [
      url(r'^$', home, name="home"),
      url(r'^apropos/$', about, name="about")
    ]
