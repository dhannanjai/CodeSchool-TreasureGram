from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.homepage_view,name='home'),
    path('post_url/',views.post_treasure_view, name='post_treasure'),
    re_path(r'^([0-9]+)/$', views.details_view, name='detail'),
    re_path(r'^user/(\w+)/$',views.user_profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout')
]