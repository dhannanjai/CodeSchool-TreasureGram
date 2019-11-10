from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.homepage_view),
    re_path(r'^([0-9]+)/$', views.details_view, name='detail'),
]