from django.shortcuts import render
from django.http import HttpResponse

def view_my_plans(request):
    return HttpResponse("all my plans")

def view_available_plans(request):
    return HttpResponse("all available plans")

def view_joined_plans(request):
    return HttpResponse("joined plans")

def view_plan_detail(request):
    return HttpResponse("plan detail")