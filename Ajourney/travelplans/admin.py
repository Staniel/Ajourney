from django.contrib import admin
from travelplans.models import Plan, JoinedPlan, PrivatePlan
# Register your models here.
admin.site.register(Plan)
admin.site.register(JoinedPlan)
admin.site.register(PrivatePlan)