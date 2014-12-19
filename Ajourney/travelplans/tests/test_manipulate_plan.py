from django.test import TestCase
from travelplans.plan_manager import PlanManager
import travelplans.facebook_proxy
from datetime import datetime
from mock import patch
import mock
import facebook
from social.apps.django_app.default.models import UserSocialAuth
import pytz
from travelplans.models import Plan, JoinedPlan
from django.contrib.auth.models import User
from travelplans.my_exception import FacebookError, DatabaseError
from django.test.client import RequestFactory
from django.contrib.auth import authenticate, login
from django.utils.timezone import utc
from django.utils import unittest

#Create your tests here.
class ManipulatePlanTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='top_secret', is_active=True)
        self.unauth_user = User.objects.create(username='unauth_testuser', email='test@example.com', password='top_secret', is_active=False)
        self.user.set_password('hello') 
        self.user.save()
        self.plan1 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 3, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))
        self.plan2 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 5, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))
        self.plan3 = Plan.objects.create(holder = self.unauth_user, description="test description", destination="west place", limit = 5, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))

        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        self.assertTrue(login)

    def test_delete_plans(self):
        pm = PlanManager()
        plan_list = pm.get_plans_by_user(self.user)
        self.assertEqual(len(plan_list), 2)
        print "DDD"
        print self.plan1.id

        response_none = self.client.post('/travelplans/delete_plan/1000', {})
        self.assertEqual(response_none.status_code, 400)

        response = self.client.post('/travelplans/delete_plan/'+str(self.plan1.id), {})
        response2 = self.client.post('/travelplans/delete_plan/'+str(self.plan3.id), {})
        self.assertEqual(response.status_code, 200)
        # print response
        plan_list = pm.get_plans_by_user(self.user)
        self.assertEqual(len(plan_list), 1)
        self.client.logout()
        response3 = self.client.post('/travelplans/delete_plan/'+str(self.plan2.id), {})
        self.assertEqual(response3.status_code, 302)

    def test_create_plans(self):
        pm = PlanManager()
        plan_list = pm.get_plans_by_user(self.user)
        self.assertEqual(len(plan_list), 2)
        response = self.client.post('/travelplans/create_plan', {'holder':self.user})
        response_invalid = self.client.post('/travelplans/create_plan', {'departtime':datetime(2014,9,1,0,0,0),'returntime':datetime(2013,9,1,0,0,0)})
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response2 = self.client.post('/travelplans/create_plan', {'holder':self.unauth_user})
        self.assertEqual(response2.status_code, 302)
        response3 = self.client.post('/travelplans/create_plan', {'holder':1})

        # print response
        plan_list = pm.get_plans_by_user(self.user)
        self.assertEqual(len(plan_list), 3)

    def test_edit_plans(self):
        pm = PlanManager()

        response_none = self.client.post('/travelplans/edit_plan/1000', {'editlimit':50})
        self.assertEqual(response_none.status_code, 400)
        response = self.client.post('/travelplans/edit_plan/'+str(self.plan2.id), {'editlimit':50})
        self.assertEqual(response.status_code, 200)
        
        response_invalid = self.client.post('/travelplans/edit_plan/'+str(self.plan2.id), {'editdepart':datetime(2014,9,1,0,0,0),'editreturn':datetime(2013,9,1,0,0,0)})
