from django.shortcuts import render
from django.http import HttpResponse
from travelplans.plan_manager import PlanManager
from travelplans.models import Plan, JoinedPlan
def join_plan(request, plan_id):
	try:
		user = request.user
		if not user.is_authenticated():
			return redirect('login')
		pm = PlanManager()
		plan = pm.get_plan_by_id(plan_id)
		if pm.joinable(user, plan):
			newjoin = JoinedPlan()
			newjoin.joined_user = user
			newjoin.joined_plan = plan
			newjoin.save()
			return HttpResponse("true")
		else:
			return HttpResponse("error: unable to join")
	except Exception as e:
		return HttpResponse("error: "+str(e))

def unjoin_plan(request, plan_id):
	try:
		user = request.user
		if not user.is_authenticated():
			return redirect('login')
		pm = PlanManager()
		joined_plan=JoinedPlan.objects.get(joined_plan__exact=plan_id,joined_user__exact=user)
		joined_plan.delete()
		return HttpResponse("true")
	except Exception as e:
		return HttpResponse("error: "+str(e))

