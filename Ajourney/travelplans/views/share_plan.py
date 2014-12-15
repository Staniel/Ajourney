from django.shortcuts import render
from django.http import HttpResponse
from travelplans.facebook_proxy import share_plan_action
from travelplans.plan_manager import PlanManager
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import InternalError, DatabaseError
def share_plan(request, plan_id):
	try:
		user = request.user
		if not user.is_authenticated():
			return redirect('login')
		URL = " http://104.236.26.136/travelplans/view_plan_detail/"+str(plan_id)+"/"
		pm = PlanManager()
		comment = request.POST.get('sharecomment', "")
		plan = pm.get_plan_by_id(plan_id)
		if plan is None:
			raise Exception("plan do not exist")
		if share_plan_action(user, plan, comment+URL):
			return HttpResponse("true")
		else:
			raise Exception("share plan failed")
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
