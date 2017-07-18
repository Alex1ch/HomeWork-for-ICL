from django.conf.urls import include, url
from django.contrib import admin
from ExcelReader import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^loadfile/', views.loadView),
    url(r'^getlist', views.get_list),
    url(r'^getgraph/id=(?P<id>[0-9]+)',views.get_graph)
]
