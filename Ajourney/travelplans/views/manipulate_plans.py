from django.shortcuts import  redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from travelplans.models import Plan, PrivatePlan
from datetime import datetime
from django.template import RequestContext, loader
from travelplans.plan_manager import PlanManager
from social.apps.django_app.default.models import UserSocialAuth
def create_plan(request):
    try:
        if not request.user.is_authenticated():
            return redirect('login')
        new_plan = Plan()
        new_plan.holder = request.user
        #do validation
        new_plan.destination = request.POST.get('destination', "nonedestination")
        new_plan.description = request.POST.get('description', "nonedescript")
        new_plan.depart_time = request.POST.get('departtime', datetime.today())
        new_plan.return_time = request.POST.get('returntime', datetime.today())
        is_private = request.POST.get('isprivate', False)
        if is_private == "1":
            new_plan.is_private = True
        else:
            new_plan.is_private = False
        print "is private is "+str(new_plan.is_private)
        if new_plan.depart_time > new_plan.return_time:
            raise Exception("depart time should be before return time")
        new_plan.limit = request.POST.get('limit', 2)
        user_list = request.POST.getlist('friend',[])
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

    except Exception as e:
        #error code
        print str(e)
        pm = PlanManager()
        plan = pm.get_plan_by_id(planid)
        if plan is not None:
            plan.delete()
        return HttpResponse(str(e), status = 400)
            
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
            if plan.depart_time > plan.return_time:
                raise Exception("depart time should be before return time")
            plan.limit = request.POST.get('editlimit', 2)
            plan.save()
            return HttpResponse("true")
        else:
            raise Exception("not editable")
    except Exception as e:
        print str(e)
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
    except Exception as e:
        print str(e)
        return HttpResponse(str(e), status = 400)
