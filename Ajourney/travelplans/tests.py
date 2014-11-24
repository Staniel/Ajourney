from django.test import TestCase
from travelplans.plan_manager import PlanManager
import travelplans.facebook_proxy
from django.contrib.auth.models import User
# Create your tests here.

class PlanTestCase(TestCase):
    def test__str__(self):
        assertTrue(False)

class JoinedPlanTestCase(TestCase):
    def test__str__(self):
        assertTrue(False)

class PlanManagerTestCase(TestCase):

    def test_planmanager_get_by_id(self):
        """
        get plan by id test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertEqual(plan, None)
    def test_planmanager_get_by_destination(self):
        """
        get plan by destination test case
        """
        pm = PlanManager()
        plan = pm.get_plans_by_destination("Beijing")
        self.assertEqual(plan, None)
    def test_planmanager_get_by_time(self):
        """
        get plan by time test case
        """
        pm = PlanManager()
        plan = pm.get_plans_by_time()
        self.assertEqual(plan, None)
    def test_planmanager_get_by_user(self):
        """
        get plan by user test case
        """
        pm = PlanManager()
        user = User.objects.get(id=1)
        plan = pm.get_plan_by_user(user)
        self.assertEqual(plan, None)
    def test_planmanager_get_all_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        user = User.objects.get(id=1)
        plans = pm.get_all_plans()
        self.assertEqual(len(plans), 3)
    def test_planmanager_get_joined_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        user = User.objects.get(id=1)
        plan = pm.get_joined_plans()
        self.assertEqual(len(plan), 4)
    def test_planmanager_has_joined_plans(self):
        """
        sample test case
        """
        self.assertTrue(True)

    def test_planmanager_viewable(self):
        """
        sample test case
        """
        self.assertTrue(False)
    def test_planmanager_editable(self):
        """
        sample test case
        """
        self.assertTrue(False)
    def test_planmanager_shareable(self):
        """
        sample test case
        """
        self.assertTrue(False)
    def test_planmanager_joinable(self):
        """
        sample test case
        """
        self.assertTrue(False)


"""There are 4 users in the database: Alice, Bob, Cathy, David"""
"""Alice, Bob, David are friends, and Cathy is not friend of the aboves"""
class FacebookProxyTestCase(TestCase):
	def test_is_friend_valid(self):
		Alice = User.objects.get(username__exact='Alice')
		Bob = User.objects.get(username__exact='Bob')
		ret = travelplans.facebook_proxy.is_friend(Alice, Bob)
		self.assertTrue(ret)
		ret = travelplans.facebook_proxy.is_friend(Alice, Bob)
		self.assertTrue(ret)

	def test_all_friends_valid(self):
		Alice = User.objects.get(username__exact='Alice')
		Bob = User.objects.get(username__exact='Bob')
		David = User.objects.get(username__exact='David')
		David = User.objects.get()
		flist = all_friends(alice)
		self.assertTrue(len(flist) == 2 and Bob in flist and David in flist)

	def test_all_friends_exception(self):
		Cathy = User.obejects.get(username__exact='Cathy')
		self.assertRaises(NoFriendsException,all_friends,Csathy)

class SocialAuthExceptionMiddlewareTestCase(TestCase):
    def test_process_exception(self):
        assertTrue(False)

class SharePlanTestCase(TestCase):
	def test_share_plan(self):
        self.assertTrue(False)
class JoinPlanTestCase(TestCase):
	def test_join_plan(self):
        self.assertTrue(False)
class ManipulatePlanTestCase(TestCase):
	def test_manipulate_plan_create(self):
        self.assertTrue(False)
	def test_manipulate_plan_edit(self):
        self.assertTrue(False)
	def test_manipulate_plan_delete(self):
        self.assertTrue(False)

class ViewPlanTestCase(TestCase):
	def test_view_available_plans(self):
        self.assertTrue(False)
	def test_view_my_plans(self):
        self.assertTrue(False)
	def test_view_joined_plans(self):
        self.assertTrue(False)
	def test_view_plan_detail(self):
        self.assertTrue(False)


