from travelplans.models import Plan

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

def get_all_plans():
	return Plan.objects.all()

def viewable(user,plan):
	return True

def editable(user,plan):
	return True

def sharable(user,plan):
	return True

def joinable(user,plan):
	return True




