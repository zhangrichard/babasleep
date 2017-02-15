from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^detail/$', views.post_detail, name='detail'),
    url(r'^list/$', views.post_list, name='list'),
    url(r'^delete/$', views.post_delete, name='delete'),
]