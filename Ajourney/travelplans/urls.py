from django.conf.urls import patterns, url

from travelplans import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
