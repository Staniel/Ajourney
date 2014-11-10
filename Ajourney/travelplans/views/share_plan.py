from django.shortcuts import render
from django.http import HttpResponse
from travelplans.facebook_proxy import share_plan_action
from travelplans.plan_manager import PlanManager
def share_plan(request, plan_id):
	try:
		URL = ""
		pm = PlanManager()
		comment = request.POST.get('sharecomment', "")
		user = request.user
		plan = pm.get_plan_by_id(plan_id)
		if user.is_authenticated() and share_plan_action(user, plan, comment+URL):
			return HttpResponse("true")
		else:
			return HttpResponse("error: share plan failed")
	except Exception as e:
		return HttpResponse("error: "+str(e))
