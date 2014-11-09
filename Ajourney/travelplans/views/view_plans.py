from django.http import HttpResponse
from django.template import RequestContext, loader
from travelplans.plan_manager import get_plans_by_destination,get_all_plans,get_plan_by_id


def view_plans(request):
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
        'list_title': "All Available Plans",
    })
    return HttpResponse(template.render(context))


def available_plans(request):
	plan_list=get_all_plans()
	template = loader.get_template('travelplans/planlist.html')
	context = RequestContext(request, {
        'plan_list': plan_list,
        'list_title': "All Available Plans",
    })
	return HttpResponse(template.render(context))

def my_plans(request):
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/planlist.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
        'list_title': "All My Plans",
    })
    return HttpResponse(template.render(context))

def joined_plans(request):
    plan_list=get_all_plans()
    template = loader.get_template('travelplans/planlist.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
        'list_title': "All Joined Plans",
    })
    return HttpResponse(template.render(context))

def view_plan_detail(request):
    planid=request.GET.get('planid')
    plan=get_plan_by_id(planid)
    user=plan.get_holder()
    is_friend=True
    template = loader.get_template('travelplans/plan_detail.html')
    context = RequestContext(request, {
        'plan': plan,
        'current_user': user,
        'is_friend':is_friend,
    })
    return HttpResponse(template.render(context))