from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signin$', views.CreateUserView.as_view(), name='signup'),
    url(r'^login$', views.login, name='loginuser'),
    url(r'^home$', views.update_profile, name='update'), 
    url(r'^logout$', auth_views.logout, name='logout'),
]