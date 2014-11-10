from django.test import TestCase
from travelplans.plan_manager import PlanManager
import travelplans.facebook_proxy
from django.contrib.auth.models import User
# Create your tests here.
class PlanManagerTestCase(TestCase):

    def test_planmanager_get_by_id_plan(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertEqual(plan, None)


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
		flist = all_friends(alice);
			self.assertTrue(len(flist) == 2 and Bob in flist and David in list)

	def test_all_friends_exception(self):
		Cathy = User.obejects.get(username__exact='Cathy')
		self.assertRaises(NoFriendsException,all_friends,Csathy)



