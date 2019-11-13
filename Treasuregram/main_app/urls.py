from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.homepage_view,name='home'),
    path('post_url/',views.post_treasure_view, name='post_treasure'),
    re_path(r'^([0-9]+)/$', views.details_view, name='detail'),
    
]