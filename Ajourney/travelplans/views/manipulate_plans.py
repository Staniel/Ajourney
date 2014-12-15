from django.shortcuts import  redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from travelplans.models import Plan, PrivatePlan
from datetime import datetime
from django.template import RequestContext, loader
from travelplans.plan_manager import PlanManager
from social.apps.django_app.default.models import UserSocialAuth
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import InternalError, DatabaseError

def create_exception_handler(planid):
    pm = PlanManager()
    plan = pm.get_plan_by_id(planid)
    if plan is not None:
        plan.delete()

def check_plan(plan):
    if not plan.destination:
        print "enter check"
        raise Exception("destination can not be empty")
    if not plan.depart_time:
        raise Exception("depart_time can not be empty")
    if not plan.return_time:
        raise Exception("return_time can not be empty")
    if plan.depart_time > plan.return_time:
        raise Exception("depart time should be before return time")
    if not plan.limit:
        raise Exception("limit can not be empty")
    if int(plan.limit) < 2:
        raise Exception("limit should be at least two")

def create_plan(request):
    new_plan = Plan()
    try:
        if not request.user.is_authenticated():
            return redirect('login')
        new_plan.holder = request.user
        #do validation
        new_plan.destination = request.POST.get('destination', "nonedestination")
        new_plan.description = request.POST.get('description', "nonedescript")
        new_plan.depart_time = request.POST.get('departtime', datetime.today())
        new_plan.return_time = request.POST.get('returntime', datetime.today())
        new_plan.limit = request.POST.get('limit', 2)
        user_list = request.POST.getlist('friend',[])
        is_private = request.POST.get('isprivate', False)
        if is_private == "1":
            new_plan.is_private = True
        else:
            new_plan.is_private = False
        check_plan(new_plan)
        new_plan.save()
        planid = new_plan.id
        if new_plan.is_private:
            for facebookid in user_list:
                auth_user = UserSocialAuth.objects.filter(uid__exact=facebookid)
                currentuser=User.objects.filter(id__exact=auth_user[0].user_id)
                accessible_user = currentuser[0]
                newPrivatePlan = PrivatePlan()
                newPrivatePlan.accessible_user = accessible_user
                newPrivatePlan.accessible_plan = new_plan
                newPrivatePlan.save()
        return HttpResponse("true");
    except ObjectDoesNotExist as e:
        create_exception_handler(new_plan.id)
        return HttpResponse(str(e), status=404)
    except PermissionDenied as e:
        create_exception_handler(new_plan.id)
        return HttpResponse(str(e), status=403)
    except DatabaseError as e:
        create_exception_handler(new_plan.id)
        return HttpResponse(str(e), status=503)
    except InternalError as e:
        create_exception_handler(new_plan.id)
        return HttpResponse(str(e), status=500)
    except Exception as e:
        create_exception_handler(new_plan.id)
        return HttpResponse(str(e), status=400)
def edit_plan(request, plan_id):
    try:    
        if not request.user.is_authenticated():
            return redirect('login')
        pm = PlanManager()
        #flake 8 
        plan = pm.get_plan_by_id(plan_id)
        if plan is None:
            raise Exception("plan not exist")
        if pm.editable(request.user, plan):
            plan.destination = request.POST.get('editdestination', "nonedestination");
            plan.description = request.POST.get('editdescription', "nonedestination");
            plan.depart_time = request.POST.get('editdepart', datetime.today())
            plan.return_time = request.POST.get('editreturn', datetime.today())
            plan.limit = request.POST.get('editlimit', 2)
            check_plan(plan)
            plan.save()
            return HttpResponse("true")
        else:
            raise Exception("not editable")

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

def delete_plan(request, plan_id):
    try:
        if not request.user.is_authenticated():
            return redirect('login')
        pm=PlanManager()
        plan = pm.get_plan_by_id(plan_id)
        if plan is None:
            raise Exception("plan not exist")
        if pm.editable(request.user, plan):
            plan.delete()
            return HttpResponse("true")
        else:
            raise Exception("not editable")
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
