from django.test import TestCase
from travelplans.plan_manager import PlanManager
from django.contrib.auth.models import User
# Create your tests here.
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
        user = User.models.get(id=1)
        plan = pm.get_plan_by_user(user)
        self.assertEqual(plan, None)
    def test_planmanager_get_all_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        plans = pm.get_all_plans()
        self.assertEqual(len(plans), 3)
    def test_planmanager_get_joined_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_joined_plans()
        self.assertEqual(len(plan), 4)
    def test_planmanager_has_joined_plans(self):
        """
        sample test case
        """
        pm = PlanManager()
        self.assertTrue(True)

    def test_planmanager_viewable(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertTrue(True)
    def test_planmanager_editable(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertTrue(True)
    def test_planmanager_shareable(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertTrue(True)
    def test_planmanager_joinable(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertTrue(True)

