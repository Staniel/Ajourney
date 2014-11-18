from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^$', 'travelplans.views.login.facebook_login', name='login'),
    url(r'^travelplans/', include('travelplans.urls', namespace="travelplans")),
    url(r'^admin/', include(admin.site.urls)),

	url('', include('django.contrib.auth.urls', namespace='auth')),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^', 'travelplans.views.error_views.error_view',name='error_view'),
)
