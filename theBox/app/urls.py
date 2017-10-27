from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^scan', views.scan, name="KicomAVscan"),
    url(r'^ssh', views.ssh, name="ssh"),
    url(r'^vtscan', views.vtscan, name="vtScan"),
    url(r'^command/(?P<cmd>\D+)', views.cmd),
]