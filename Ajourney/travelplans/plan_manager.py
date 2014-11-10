from travelplans.models import Plan,JoinedPlan
from facebook_proxy import is_friend,all_friends

'''
Get list of Plan objects whose destination is exactly des, case insensitive.
'''
def get_plans_by_destination(des):
	plan_list=Plan.objects.filter(destination__iexact=des)
	return plan_list

'''
Get list of Plan objects whose depart_time and return_time are within depart and return.
depart 'xxxx-xx-xx'
return 'xxxx-xx-xx'
'''
def get_plans_by_time(depart_d,return_d):
	plan_list=Plan.objects.filter(depart_time__gte=depart_d,return_time__lte=return_d)
	return plan_list

'''
Get list of plans whose owner is user
'''
def get_plans_by_user(user):
	plan_list=Plan.objects.filter(holder__exact=user)
	return plan_list

def get_plan_by_id(planid):
	try:
		plan=Plan.objects.get(id__exact=planid)
		return plan
	except:
		return None

def get_all_plans():
	return Plan.objects.all()

def get_all_joiners(plan):
	joiners=[]
	joinedplans=JoinedPlan.objects.filter(joined_plan__exact=plan)
	for joinedplan in joinedplans:
		joiners.append(joinedplan.joined_user)
	return joiners

def viewable(user,plan):
	is_friend=is_friend(user,plan.holder)
	if user.is_superuser or useruser==plan.holder or is_friend:
		return True
	else:
		return False

def editable(user,plan):
	if user.is_superuser or user==plan.holder:
		return True
	else:
		return False

def sharable(user,plan):
	if not user.is_superuser:
		return True
	else:
		return False

def joinable(user,plan):
	if user.is_superuser:
		return False
	else:
		is_friend=is_friend(user,plan.holder)
		joiners=get_all_joiners(plan)
		if is_friend and user not in joiners:
			return True
		else:
			return False




