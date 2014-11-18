from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render,redirect,render_to_response


def error_view(request):
    return render_to_response('travelplans/error.html',{'error_message':'This page does not exist.'})
