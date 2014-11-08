from django.http import HttpResponse
from django.template import RequestContext, loader
from travelplans.plan_manager import get_plans_by_destination,get_all_plans

def view_my_plans(request):
    return HttpResponse("all my plans")

def view_available_plans(request):
	plan_list=get_all_plans()
	template = loader.get_template('travelplans/planlist.html')
	context = RequestContext(request, {
        'plan_list': plan_list,
    })
	return HttpResponse(template.render(context))

def view_joined_plans(request):
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
    })
    return HttpResponse(template.render(context))

def view_plan_detail(request):
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
    })
    return HttpResponse(template.render(context))