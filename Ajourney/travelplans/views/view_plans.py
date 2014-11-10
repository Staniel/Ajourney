from django.http import HttpResponse
from django.template import RequestContext, loader
from travelplans.plan_manager import PlanManager
from django.shortcuts import render,redirect

def available_plans(request):
    user=request.user
    pm=PlanManager()
    available_plans=pm.get_all_available_plans(user)
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': available_plans,
        'list_title': "All Available Plans",
    })
    return HttpResponse(template.render(context))

def my_plans(request):
    user=request.user
    pm=PlanManager()
    my_plans=pm.get_plans_by_user(user)
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': my_plans,
        'list_title': "All My Plans",
    })
    return HttpResponse(template.render(context))

def joined_plans(request):
    user=request.user
    pm=PlanManager()
    joined_plans=pm.get_joined_plans(user)
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': joined_plans,
        'list_title': "All Joined Plans",
    })
    return HttpResponse(template.render(context))

def view_plan_detail(request,planid):
    user=request.user
    pm=PlanManager()
    plan=pm.get_plan_by_id(planid)
    if plan and pm.viewable(user,plan):
        template = loader.get_template('travelplans/plan_detail.html')
        context = RequestContext(request, {
        'plan': plan,
        'editable':pm.editable(user,plan),
        'sharable':pm.sharable(user,plan),
        'joinable':pm.joinable(user,plan),
        'joiners':pm.get_all_joiners(plan),
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponse("This plan is not available.")