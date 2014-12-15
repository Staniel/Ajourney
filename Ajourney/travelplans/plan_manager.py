from travelplans.models import Plan,JoinedPlan, PrivatePlan
from facebook_proxy import is_friend

class PlanManager(object):
	
	'''
	Get list of Plan objects whose destination is exactly des, case insensitive.
	'''
	def get_plans_by_destination(self,des):
		plan_list=Plan.objects.filter(destination__iexact=des)
		return plan_list

	'''
	Get list of Plan objects whose depart_time and return_time are within depart and return.
	depart 'xxxx-xx-xx'
	return 'xxxx-xx-xx'
	'''
	def get_plans_by_time(self,depart_d,return_d):
		plan_list=Plan.objects.filter(depart_time__gte=depart_d,return_time__lte=return_d)
		return plan_list

	'''
	Get list of plans whose owner is user
	'''
	def get_plans_by_user(self,user):
		plan_list=Plan.objects.filter(holder__exact=user)
		return plan_list

	def get_plan_by_id(self,planid):
		try:
			plan=Plan.objects.get(id__exact=planid)
			return plan
		except:
			return None

	def get_all_plans(self):
		return Plan.objects.all()


	def get_all_joiners(self,plan):
		joiners=[]
		joinedplans=JoinedPlan.objects.filter(joined_plan__exact=plan)
		for joinedplan in joinedplans:
			joiners.append(joinedplan.joined_user)
		return joiners

	def get_joined_plans(self,user):
		plans=[]
		joinedplans=JoinedPlan.objects.filter(joined_user__exact=user)
		for joinedplan in joinedplans:
			plans.append(joinedplan.joined_plan)
		return plans

	def has_joined_plan(self,user,plan):
		try:
			joinedplans=JoinedPlan.objects.get(joined_plan__exact=plan,joined_user__exact=user)
			return True
		except:
			return False

	def get_all_available_plans(self,user):
		plan_list=self.get_all_plans()
		available_plans=[]
		for plan in plan_list:
			if self.viewable(user,plan):
				available_plans.append(plan)
		return available_plans

	def viewable(self,user,plan):
		if plan is None:
			return False
		if user == plan.holder or user.is_superuser or plan.holder.is_superuser:
			return True
		if plan.is_private:
			if PrivatePlan.objects.filter(accessible_user=user, accessible_plan=plan).exists():
				return True
			else:
				return False
		if is_friend(user,plan.holder):
			return True
		else:
			return False

	def editable(self,user,plan):
		if plan is None:
			return False
		if user.is_superuser or user==plan.holder:
			return True
		else:
			return False

	def sharable(self,user,plan):
		if plan is None:
			return False
		if not user.is_superuser:
			return True
		else:
			return False

	def joinable(self,user,plan):
		if plan is None:
			return False
		if user.is_superuser:
			return False
		else:
			isfriend=is_friend(user,plan.holder)
			joiners=self.get_all_joiners(plan)
			if isfriend or plan.holder.is_superuser:
				if len(joiners)<plan.limit-1 and user not in joiners:
					return True
				else:
					return False
			else:
				return False




