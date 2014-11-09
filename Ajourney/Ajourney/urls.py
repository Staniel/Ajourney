from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ajourney.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^travelplans/', include('travelplans.urls', namespace="travelplans")),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^facebook/', include('django_facebook.urls')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^$', 'travelplans.views.views.home', name='home'),
)
