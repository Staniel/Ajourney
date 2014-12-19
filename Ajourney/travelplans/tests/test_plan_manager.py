from django.test import TestCase
from travelplans.plan_manager import PlanManager
import travelplans.facebook_proxy
from datetime import datetime
from travelplans import plan_manager

import pytz
from travelplans.models import Plan, JoinedPlan
from django.contrib.auth.models import User

from django.test.client import RequestFactory
from django.contrib.auth import authenticate, login
from django.utils.timezone import utc
from django.utils import unittest

#Create your tests here.
class PlanManagerTestCase(TestCase):
    def setUp(self):
        self.super = User.objects.create(username='super', email='test@example.com', password='top_secret', is_active=True, is_superuser=True)
        self.user = User.objects.create(username='testuser', email='test@example.com', password='top_secret', is_active=True)
        self.user2 = User.objects.create(username='testuser2', email='test@example.com', password='top_secret', is_active=True)
        self.plan1 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 3, depart_time = datetime(2014,9,1,0,0,0), return_time = datetime(2014,9,8,0,0,0))
        self.plan2 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 5, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))
        self.plan3 = Plan.objects.create(holder = self.user, description="test description", destination="east place", limit = 5, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))
        self.plan4 = Plan.objects.create(holder = self.user2, description="test description", destination="north place", limit = 5, depart_time = datetime.utcnow().replace(tzinfo=utc), return_time = datetime.utcnow().replace(tzinfo=utc))

        JoinedPlan.objects.create(joined_user = self.user, joined_plan = self.plan4)
        JoinedPlan.objects.create(joined_user = self.user2, joined_plan = self.plan1)
        JoinedPlan.objects.create(joined_user = self.user2, joined_plan = self.plan2)
    def test_planmanager_get_by_id(self):
        """
        get plan by id test case
        """
        pm = PlanManager()

        plan_none = pm.get_plan_by_id(999)
        self.assertEqual(plan_none, None)
        plan_1 = pm.get_plan_by_id(self.plan1.id)
        self.assertEqual(plan_1.holder, self.user)
        self.assertEqual(plan_1.description, "test description")
        self.assertEqual(plan_1.destination, "west place")
        self.assertEqual(plan_1.limit, 3)
        self.assertEqual(plan_1.depart_time,  pytz.utc.localize(datetime(2014,9,1,0,0,0)))
        self.assertEqual(plan_1.return_time,  pytz.utc.localize(datetime(2014,9,8,0,0,0)))

    def test_viewable(self):
        pass


    def test_planmanager_get_by_destination(self):
        """
        get plan by destination test case
        """
        print "destinatiom"
        pm = PlanManager()
        plan_list = pm.get_plans_by_destination("west place")
        self.assertEqual(len(plan_list), 2)
    def test_planmanager_get_by_time(self):
        """
        get plan by time test case
        """
        pm = PlanManager()
    def test_planmanager_get_by_user(self):
        """
        get plan by user test case
        """
        pm = PlanManager()
        plan_list = pm.get_plans_by_user(self.user)
        self.assertEqual(len(plan_list), 3)
        plan_list2 = pm.get_plans_by_user(self.user2)
        self.assertEqual(len(plan_list2), 1)

    def test_planmanager_get_all_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan_list = pm.get_all_plans()
        self.assertEqual(len(plan_list), 4)
    def test_planmanager_get_all_joiners(self):
        pm = PlanManager()
        user_list = pm.get_all_joiners(self.plan4)
        self.assertEqual(len(user_list), 1)
        self.assertEqual(user_list[0], self.user)
    def test_planmanager_get_joined_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan_list1 = pm.get_joined_plans(self.user)
        self.assertEqual(len(plan_list1), 1)
        self.assertEqual(plan_list1[0].destination, "north place")
        plan_list2 = pm.get_joined_plans(self.user2)
        self.assertEqual(len(plan_list2), 2)

    def test_planmanager_has_joined_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        self.assertTrue(pm.has_joined_plan(self.user, self.plan4))
        self.assertFalse(pm.has_joined_plan(self.user, self.plan3))
       
    def test_planmanager_viewable(self):
        pm = PlanManager()
        ret1 = pm.viewable(self.super, None)
        self.assertFalse(ret1)
        ret2 = pm.viewable(self.super, self.plan1)
        self.assertTrue(ret2)
        
        
    def test_planmanager_editable(self):
        pm = PlanManager()
        ret1 = pm.editable(self.super, None)
        self.assertFalse(ret1)
        ret2 = pm.editable(self.super, self.plan1)
        self.assertTrue(ret2)
        
    def test_planmanager_sharable(self):
        pm = PlanManager()
        ret1 = pm.sharable(self.super, None)
        self.assertFalse(ret1)
        ret2 = pm.sharable(self.super, self.plan1)
        self.assertFalse(ret2)
        ret3 = pm.sharable(self.user, self.plan1)
        self.assertTrue(ret3)
        
    def test_planmanager_joinable(self):
        pm = PlanManager()
        ret1 = pm.joinable(self.user, None)
        self.assertFalse(ret1)
        ret2 = pm.joinable(self.super, self.plan1)
        self.assertFalse(ret2)
        ret3 = pm.joinable(self.user, self.plan1)
        self.assertFalse(ret3)