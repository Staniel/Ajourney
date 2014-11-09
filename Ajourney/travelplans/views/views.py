from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import urllib2
import json

# Create your views here.
def index(request):
	context = {'test': 1}
	return render(request, 'travelplans/index.html', context)



def home(request):
#       context = RequestContext(request,
#                           {'request': request,
#                           'user': request.user})
        if hasattr(request.user, 'social_auth'):
            social_user = request.user.social_auth.filter( provider='facebook',).first()
            if social_user:
                url = u'https://graph.facebook.com/{0}/' \
                    u'friends?fields=id,name,location,picture' \
                    u'&access_token={1}'.format(social_user.uid,
                social_user.extra_data['access_token'],
            )
                response = urllib2.Request(url)
                friends = json.loads(urllib2.urlopen(response).read()).get('data')
                context = RequestContext(request, {'request': request, 'user': request.user, 'friends': friends})
                return render_to_response('travelplans/view_plans.html',context_instance=context)
        else:
                friends = None;
        context = RequestContext(request, {'request': request, 'user': request.user, 'friends': friends})

        return render_to_response('travelplans/home.html',context_instance=context)