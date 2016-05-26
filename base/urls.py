from django.conf.urls import url
from .views import home, about, tv_display

app_name = "base"
urlpatterns = [
      url(r'^$', home, name="home"),
      url(r'^tv_display/$', tv_display, name="tv_display"),
      url(r'^apropos/$', about, name="about"),
    ]
