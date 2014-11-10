from django.test import TestCase

# Create your tests here.
class Tests(TestCase):

    def test_sample(self):
        """
        sample test case
        """
        a = False
        self.assertEqual(a, True)
