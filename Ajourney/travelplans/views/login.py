from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from travelplans.models import User
from social.apps.django_app.default.models import UserSocialAuth
from django.contrib.auth import login,authenticate,logout
import facebook
import urllib2
import json

def facebook_login(request):
    friends = None
    if hasattr(request.user, 'social_auth'):
        social_user = request.user.social_auth.filter(provider='facebook',).first()
        if social_user:
            try:
                graph = facebook.GraphAPI(social_user.extra_data['access_token'])
                profile = graph.get_object("me")
                facebookid=profile['id']
                usersocialauth=UserSocialAuth.objects.filter(uid__exact=facebookid)
                if len(usersocialauth)>0:
                    currentuser=User.objects.filter(id__exact=usersocialauth[0].user_id)
                    if len(currentuser)==1:
                        currentuser=currentuser[0]
                        currentuser.backend = 'django.contrib.auth.backends.ModelBackend'
                        if currentuser and currentuser.is_active:
                            login(request,currentuser)
                            return redirect('travelplans/')
            except Exception as e:
                print str(e)
                logout(request)
                return HttpResponse("in login view"+str(e))
                # return render_to_response('travelplans/login.html')
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('travelplans/login.html',context_instance=context)