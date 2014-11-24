from django.test import TestCase
from travelplans.plan_manager import PlanManager
import travelplans.facebook_proxy
from datetime import datetime
<<<<<<< HEAD
import pytz
from travelplans.models import Plan
=======
from travelplans.models import Plan, JoinedPlan
>>>>>>> 879e5626bc757ae3552ab9939e35a6a2114f8dd6
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.contrib.auth import authenticate, login

<<<<<<< HEAD
#   Create your tests here.
class PlanManagerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='top_secret', is_active=True)
        self.user.set_password('hello') 
        self.user.save()
        self.plan1 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 3, depart_time = datetime(2014,9,1,0,0,0), return_time = datetime(2014,9,1,0,0,0))
        self.plan2 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 5, depart_time = datetime.today(), return_time = datetime.today())
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        self.assertTrue(login)

    def test_planmanager_get_by_id(self):
        """
        get plan by id test case
        """
        pm = PlanManager()
        plan_none = pm.get_plan_by_id(999)
        self.assertEqual(plan_none, None)
        plan_1 = pm.get_plan_by_id(1)
        self.assertEqual(plan_1.holder, self.user)
        self.assertEqual(plan_1.description, "test description")
        self.assertEqual(plan_1.destination, "west place")
        self.assertEqual(plan_1.limit, 3)
        self.assertEqual(plan_1.depart_time,  pytz.utc.localize(datetime(2014,9,1,0,0,0)))
        self.assertEqual(plan_1.return_time,  pytz.utc.localize(datetime(2014,9,1,0,0,0)))



    # def test_planmanager_get_by_destination(self):
    #     """
    #     get plan by destination test case
    #     """
    #     pm = PlanManager()
    #     plan = pm.get_plans_by_destination("Beijing")
    #     self.assertEqual(plan, None)
    # def test_planmanager_get_by_time(self):
    #     """
    #     get plan by time test case
    #     """
    #     pm = PlanManager()
    #     plan = pm.get_plans_by_time()
    #     self.assertEqual(plan, None)
    # def test_planmanager_get_by_user(self):
    #     """
    #     get plan by user test case
    #     """
    #     pm = PlanManager()
    #     user = User.objects.get(id=1)
    #     plan = pm.get_plan_by_user(user)
    #     self.assertEqual(plan, None)
    # def test_planmanager_get_all_plans(self):
    #     """
    #     sample test case
    #     """
    #     pm = PlanManager()
    #     user = User.objects.get(id=1)
    #     plans = pm.get_all_plans()
    #     self.assertEqual(len(plans), 3)
    # def test_planmanager_get_joined_plans(self):
    #     """
    #     sample test case
    #     """
    #     pm = PlanManager()
    #     user = User.objects.get(id=1)
    #     plan = pm.get_joined_plans()
    #     self.assertEqual(len(plan), 4)
    # def test_planmanager_has_joined_plans(self):
    #     """
    #     sample test case
    #     """
    #     self.assertTrue(True)

    # def test_planmanager_viewable(self):
    #     """
    #     sample test case
    #     """
    #     self.assertTrue(False)
    # def test_planmanager_editable(self):
    #     """
    #     sample test case
    #     """
    #     self.assertTrue(False)
    # def test_planmanager_shareable(self):
    #     """
    #     sample test case
    #     """
    #     self.assertTrue(False)
    # def test_planmanager_joinable(self):
    #     """
    #     sample test case
    #     """
    #     self.assertTrue(False)
=======
# Create your tests here.
class PlanManagerTestCase(TestCase):
    def setUp(self):
        self.super = User.objects.create(username='super', email='test@example.com', password='top_secret', is_active=True, is_superuser=True)
        self.user = User.objects.create(username='testuser', email='test@example.com', password='top_secret', is_active=True)
        self.user2 = User.objects.create(username='testuser2', email='test@example.com', password='top_secret', is_active=True)
        self.plan1 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 3, depart_time = datetime.today(), return_time = datetime.today())
        self.plan2 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 5, depart_time = datetime.today(), return_time = datetime.today())
        self.plan3 = Plan.objects.create(holder = self.user, description="test description", destination="east place", limit = 5, depart_time = datetime.today(), return_time = datetime.today())
        self.plan4 = Plan.objects.create(holder = self.user2, description="test description", destination="north place", limit = 5, depart_time = datetime.today(), return_time = datetime.today())
        JoinedPlan.objects.create(joined_user = self.user, joined_plan = self.plan4)
        JoinedPlan.objects.create(joined_user = self.user2, joined_plan = self.plan1)
        JoinedPlan.objects.create(joined_user = self.user2, joined_plan = self.plan2)
    def test_planmanager_get_by_id(self):
        """
        get plan by id test case
        """
        pm = PlanManager()
        # plan = pm.get_plan_by_id(999)
        # self.assertEqual(plan, None)
    def test_planmanager_get_by_destination(self):
        """
        get plan by destination test case
        """
        pm = PlanManager()
        plan_list = pm.get_plans_by_destination("west place")
        self.assertEqual(len(plan_list), 2)
    def test_planmanager_get_by_time(self):
        """
        get plan by time test case
        """
        pm = PlanManager()
        # plan = pm.get_plans_by_time()
        # self.assertEqual(plan, None)
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
        # user = User.objects.get(id=1)
        # plans = pm.get_all_plans()
        # self.assertEqual(len(plans), 3)
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
        """
        sample test case
        """
        pm = PlanManager()
        self.assertTrue(pm.viewable(self.user, self.plan1))
        self.assertTrue(pm.viewable(self.user, self.plan4))
        self.assertFalse(pm.viewable(self.user, None))
        self.assertTrue(pm.viewable(self.super, self.plan4))

        # self.assertTrue(False)
    def test_planmanager_editable(self):
        """
        sample test case
        """
        pm = PlanManager()
        self.assertTrue(pm.editable(self.user, self.plan1))
        self.assertFalse(pm.editable(self.user, self.plan4))
        self.assertFalse(pm.editable(self.user, None))
        self.assertTrue(pm.editable(self.super, self.plan4))
        # self.assertTrue(False)
    def test_planmanager_shareable(self):
        """
        sample test case
        """
        pm = PlanManager()
        self.assertTrue(pm.sharable(self.user, self.plan1))
        self.assertTrue(pm.sharable(self.user, self.plan4))
        self.assertFalse(pm.sharable(self.super, None))
        self.assertFalse(pm.sharable(self.super, self.plan1))


        # self.assertTrue(False)
    def test_planmanager_joinable(self):
        """
        sample test case
        """
        # self.assertTrue(False)
>>>>>>> 879e5626bc757ae3552ab9939e35a6a2114f8dd6


# """There are 4 users in the database: Alice, Bob, Cathy, David"""
# """Alice, Bob, David are friends, and Cathy is not friend of the aboves"""
# class FacebookProxyTestCase(TestCase):
# 	def test_is_friend_valid(self):
# 		Alice = User.objects.get(username__exact='Alice')
# 		Bob = User.objects.get(username__exact='Bob')
# 		ret = travelplans.facebook_proxy.is_friend(Alice, Bob)
# 		self.assertTrue(ret)
# 		ret = travelplans.facebook_proxy.is_friend(Alice, Bob)
# 		self.assertTrue(ret)

# 	def test_all_friends_valid(self):
# 		Alice = User.objects.get(username__exact='Alice')
# 		Bob = User.objects.get(username__exact='Bob')
# 		David = User.objects.get(username__exact='David')
# 		David = User.objects.get()
# 		flist = all_friends(alice)
# 		self.assertTrue(len(flist) == 2 and Bob in flist and David in flist)

# 	def test_all_friends_exception(self):
# 		Cathy = User.obejects.get(username__exact='Cathy')
# 		self.assertRaises(NoFriendsException,all_friends,Csathy)

# class SharePlanTestCase(TestCase):
# 	def test_share_plan(self):
#         self.assertTrue(False)
# class JoinPlanTestCase(TestCase):
# 	def test_join_plan(self):
#         self.assertTrue(False)
# class ManipulatePlanTestCase(TestCase):
# 	def test_manipulate_plan_create(self):
#         self.assertTrue(False)
# 	def test_manipulate_plan_edit(self):
#         self.assertTrue(False)
# 	def test_manipulate_plan_delete(self):
#         self.assertTrue(False)

# class ViewPlanTestCase(TestCase):
# 	def test_view_available_plans(self):
#         self.assertTrue(False)
# 	def test_view_my_plans(self):
#         self.assertTrue(False)
# 	def test_view_joined_plans(self):
#         self.assertTrue(False)
# 	def test_view_plan_detail(self):
#         self.assertTrue(False)


# class ManipulatePlanTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser', email='test@example.com', password='top_secret', is_active=True)
#         self.user.set_password('hello') 
#         self.user.save()
#         self.plan1 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 3, depart_time = datetime.today(), return_time = datetime.today())
#         self.plan2 = Plan.objects.create(holder = self.user, description="test description", destination="west place", limit = 5, depart_time = datetime.today(), return_time = datetime.today())
#         self.user = authenticate(username='testuser', password='hello')
#         login = self.client.login(username='testuser', password='hello')
#         self.assertTrue(login)
<<<<<<< HEAD

=======
>>>>>>> 879e5626bc757ae3552ab9939e35a6a2114f8dd6
#     def test_delete_plans(self):
#         pm = PlanManager()
#         plan_list = pm.get_plans_by_user(self.user)
#         self.assertEqual(len(plan_list), 2)
<<<<<<< HEAD
#         response = self.client.post('/travelplans/delete_plan/1/', {})
#         self.assertEqual(response.status_code, 200)
#         print response
#         plan_list = pm.get_plans_by_user(self.user)
#         self.assertEqual(len(plan_list), 1)

#     def test_edit_plans(self):
#         pm = PlanManager()
#         plan_list = pm.get_plans_by_user(self.user)
#         #   self.assertEqual(len(plan_list), 2)
#         response = self.client.post('/travelplans/edit_plan/1/', {})
#         #self.assertEqual(response.status_code, 200)

#     def test_create_plans(self):
#         pm = PlanManager()
#         plan_list = pm.get_plans_by_user(self.user)
#         #   self.assertEqual(len(plan_list), 2)
#         response = self.client.post('/travelplans/create_plan/', {})
#         self.assertEqual(response.status_code, 200)

=======
#         response = self.client.post('/travelplans/delete_plan/1', {})
#         self.assertEqual(response.status_code, 200)
        # print response
        # plan_list = pm.get_plans_by_user(self.user)
        # self.assertEqual(len(plan_list), 1)
    # def test_create_plans(self):
    #     pm = PlanManager()
    #     plan_list = pm.get_plans_by_user(self.user)
    #     self.assertEqual(len(plan_list), 2)
    #     response = self.client.get('/travelplans/view_plan_detail/1/')
    #     self.assertEqual(response.status_code, 200)
        # print response
        # plan_list = pm.get_plans_by_user(self.user)
        # self.assertEqual(len(plan_list), 1)
>>>>>>> 879e5626bc757ae3552ab9939e35a6a2114f8dd6


        

  


