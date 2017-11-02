from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^scan', views.scan, name="scan"),
    url(r'^vtscan', views.vtscan, name="vtScan"),
    url(r'^command/(?P<path>\D+)', views.cmd),
]