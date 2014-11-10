from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from travelplans.models import User
from travelplans.facebook_proxy import FBuser
from social.apps.django_app.default.models import UserSocialAuth
from django.contrib.auth import login,authenticate
import facebook
import urllib2
import json

def facebook_login(request):
    friends = None
    if hasattr(request.user, 'social_auth'):
        print "home entered"
        social_user = request.user.social_auth.filter(provider='facebook',).first()
        if social_user:
            url = u'https://graph.facebook.com/{0}/' \
                u'friends?fields=id,name,location,picture' \
                u'&access_token={1}'.format(social_user.uid,
            social_user.extra_data['access_token'],)
            response = urllib2.Request(url)
            friends_json = json.loads(urllib2.urlopen(response).read()).get('data')
            friends = []
            for i in xrange(len(friends_json)):
                friends.append(FBuser(friends_json[i]['id'],friends_json[i]['name']))
            graph = facebook.GraphAPI(social_user.extra_data['access_token'])
            profile = graph.get_object("me")
            currentuser = FBuser(profile['id'],profile['name'])

            facebookid=currentuser.id
            usersocialauth=UserSocialAuth.objects.filter(uid__exact=facebookid)
            if len(usersocialauth)>0:
                currentuser=User.objects.filter(id__exact=usersocialauth[0].user_id)
                if len(currentuser)==1:
                    currentuser=currentuser[0]
                    currentuser.backend = 'django.contrib.auth.backends.ModelBackend'
                    if currentuser and currentuser.is_active:
                        login(request,currentuser)
                        return redirect('travelplans/')
                    else:
    else:
        friends = None
    context = RequestContext(request, {'request': request, 'user': request.user, 'friends': friends})
    return render_to_response('travelplans/home.html',context_instance=context)