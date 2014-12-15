from django.shortcuts import render
from django.http import HttpResponse
from travelplans.plan_manager import PlanManager
from travelplans.models import Plan, JoinedPlan
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import InternalError, DatabaseError
def join_plan(request, plan_id):
	try:
		user = request.user
		if not user.is_authenticated():
			return redirect('login')
		pm = PlanManager()
		plan = pm.get_plan_by_id(plan_id)
		if plan is None:
			raise Exception("plan not exist")
		if pm.joinable(user, plan):
			newjoin = JoinedPlan()
			newjoin.joined_user = user
			newjoin.joined_plan = plan
			newjoin.save()
			return HttpResponse("true")
		else:
			raise Exception("unable to join")
	except ObjectDoesNotExist as e:
		return HttpResponse(str(e), status = 404)
	except PermissionDenied as e:
		return HttpResponse(str(e), status = 403)
	except DatabaseError as e:
		return HttpResponse(str(e), status = 503)
	except InternalError as e:
		return HttpResponse(str(e), status = 500)
	except Exception as e:
		return HttpResponse(str(e), status = 400)

def unjoin_plan(request, plan_id):
	try:
		user = request.user
		if not user.is_authenticated():
			return redirect('login')
		pm = PlanManager()
		joined_plan=JoinedPlan.objects.get(joined_plan__exact=plan_id,joined_user__exact=user)
		joined_plan.delete()
		return HttpResponse("true")
	except ObjectDoesNotExist as e:
		return HttpResponse(str(e), status = 404)
	except PermissionDenied as e:
		return HttpResponse(str(e), status = 403)
	except DatabaseError as e:
		return HttpResponse(str(e), status = 503)
	except InternalError as e:
		return HttpResponse(str(e), status = 500)
	except Exception as e:
		return HttpResponse(str(e), status = 400)

