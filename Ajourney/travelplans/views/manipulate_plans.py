from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from view_plans import my_plans
from travelplans.models import Plan
from datetime import datetime
from django.template import RequestContext, loader
from travelplans.plan_manager import get_all_plans

def create_plan(request, user_id=1):
    user = get_object_or_404(User, pk=user_id)
    new_plan = Plan()
    new_plan.holder = user
    new_plan.destination = request.POST.get('destination', "nonedestination")
    new_plan.description = request.POST.get('description', "nonedescript")
    new_plan.depart_time = request.POST.get('departtime', datetime.today())
    new_plan.return_time = request.POST.get('returntime', datetime.today())
    new_plan.limit = request.POST.get('limit', 3)
    new_plan.save()
    # new_joined_plan = JoinedPlan()
    # new_joined_plan.joined_user = user_id
    # new_joined_plan.joined_plan = new_plan.id
    # new_joined_plan.save()
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
        'list_title': "All My Plans",
    })
    return HttpResponse(template.render(context))
    #there is some problem with redirect to another view
    # return HttpResponseRedirect(reverse('travelplans:my_plans'))
    # redirect('travelplans/my_plans')
def edit_plan(request):
    return HttpResponse("edit plan")

def delete_plan(request):
    return HttpResponse("delete plans")
