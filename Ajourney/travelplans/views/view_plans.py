from django.shortcuts import render
from django.http import HttpResponse
from travelplans.plan_manager import get_plans_by_destination

def view_my_plans(request):
    return HttpResponse("all my plans")

def view_available_plans(request):
	plan_list=get_plans_by_destination('Los Angeles')
	plan=plan_list[0].__str__
	return HttpResponse(plan_list)

def view_joined_plans(request):
    return HttpResponse("joined plans")

def view_plan_detail(request):
    return HttpResponse("plan detail")