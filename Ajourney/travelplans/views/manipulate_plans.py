from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from view_plans import my_plans
from travelplans.models import Plan
from datetime import datetime
from django.template import RequestContext, loader
from travelplans.plan_manager import get_all_plans, editable

def create_plan(request):
    try:
        user = request.user
        if user.is_authenticated():
            new_plan = Plan()
            new_plan.holder = user
            new_plan.destination = request.POST.get('destination', "nonedestination")
            new_plan.description = request.POST.get('description', "nonedescript")
            new_plan.depart_time = request.POST.get('departtime', datetime.today())
            new_plan.return_time = request.POST.get('returntime', datetime.today())
            new_plan.limit = request.POST.get('limit', 2)
            #avoid exception page, will be refactored later
            if not isinstance(new_plan.limit, int) or new_plan.limit <= 1:
                new_plan.limit = 2
            new_plan.save()
            return redirect("travelplans:view_my_plans")
    except Exception as e:
            return e
def edit_plan(request, plan_id):
    
    plan = get_object_or_404(Plan, pk=plan_id)
    if editable(request.user, plan):
        plan.destination = request.POST.get('editdestination', "nonedestination");
        plan.description = request.POST.get('editdescription', "nonedestination");
        plan.depart_time = request.POST.get('editdepart', datetime.today())
        plan.return_time = request.POST.get('editreturn', datetime.today())
        plan.limit = request.POST.get('editlimit', 2)
        plan.save()
        return redirect("travelplans:view_plan_detail", planid = plan_id)

def delete_plan(request):
    return HttpResponse("delete plans")
