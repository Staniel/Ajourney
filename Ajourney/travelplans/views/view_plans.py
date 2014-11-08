from django.http import HttpResponse
from django.template import RequestContext, loader
from travelplans.plan_manager import get_plans_by_destination

def view_my_plans(request):
    return HttpResponse("all my plans")

def view_available_plans(request):
	plan_list=get_plans_by_destination('Los Angeles')
	template = loader.get_template('travelplans/view_plans.html')
	context = RequestContext(request, {
        'plan_list': plan_list,
    })
	return HttpResponse(template.render(context))

def view_joined_plans(request):
    return HttpResponse("joined plans")

def view_plan_detail(request):
    return HttpResponse("plan detail")