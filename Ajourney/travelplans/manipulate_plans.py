from django.shortcuts import render
from django.http import HttpResponse

def create_plan(request):
    return HttpResponse("create plan")

def edit_plan(request):
    return HttpResponse("edit plan")

def delete_plan(request):
    return HttpResponse("delete plans")
