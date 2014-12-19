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

class ViewPlanTestCase(TestCase):
   def test_view_available_plans(self):
         self.assertTrue(False)
   def test_view_my_plans(self):
         self.assertTrue(False)
   def test_view_joined_plans(self):
         self.assertTrue(False)
   def test_view_plan_detail(self):
         self.assertTrue(False)