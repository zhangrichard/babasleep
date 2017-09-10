from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #    /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]