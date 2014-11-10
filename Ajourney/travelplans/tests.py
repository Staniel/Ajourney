from django.test import TestCase
from travelplans.plan_manager import PlanManager
# Create your tests here.
class PlanManagerTestCase(TestCase):

    def test_planmanager_get_by_id_plan(self):
        """
        sample test case
        """
        pm = PlanManager()
        plan = pm.get_plan_by_id(999)
        self.assertEqual(plan, None)
