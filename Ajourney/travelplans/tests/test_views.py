from django.utils import unittest

import travelplans
from travelplans.my_exception import FacebookError, DatabaseError
from social.apps.django_app.default.models import UserSocialAuth
from travelplans.models import User, Plan, JoinedPlan
from travelplans import models

from django.test.client import RequestFactory
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,render_to_response

import datetime
import urllib2
import json
import facebook
from mock import patch, MagicMock
import mock

from django.http import HttpResponse, HttpRequest
from django.template import RequestContext, loader

from travelplans.views import view_plans, share_plan, join_plan
from travelplans import facebook_proxy
from travelplans import plan_manager
from travelplans.plan_manager import PlanManager
from travelplans.facebook_proxy import get_picture_url, all_friends_names

#Create your tests here.
class ViewPlanTestCase(unittest.TestCase):

    def setUp(self):
        user1=User(username='John',is_superuser=0)
        social_auth1=UserSocialAuth(user_id=user1.id,uid='12345',provider='facebook',extra_data={'access_token':'1','id':'12345'})
        user1.save()
        user1.social_auth.add(social_auth1)
        user1.save()
        self.social_auth1=social_auth1
        self.user1=user1

        user2=User(username='Mary',is_superuser=0)
        self.user2=user2
        user2.save()

        user3=User(username='Mike',is_superuser=0)
        social_auth3=UserSocialAuth(user_id=user3.id,uid='facebookid3',provider='facebook',extra_data={'access_token':'3','id':'facebookid3'})
        user3.save()
        user3.social_auth.add(social_auth3)
        user3.save()
        self.user3=user3
        self.social_auth3=social_auth3

        plan1 = Plan(holder_id=user1.id, destination='newWorld', depart_time=datetime.date(2014, 12, 5), return_time=datetime.date(2014, 12, 6), limit = 3)
        plan1.save()
        self.plan1=plan1


    def tearDown(self):
        self.social_auth1.delete()
        self.user1.delete()
        self.user2.delete()
        self.social_auth3.delete()
        self.user3.delete()
        self.plan1.delete()
        
    
    def test_view_available_plans(self):
        request1 = HttpRequest()
        request1.user = self.user1
        
        data={'data':[
        {'id':'plan1'},
        {'id':'plan2'}
        ]}

        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth1_1:
            with patch.object(plan_manager.PlanManager,'get_all_available_plans', return_value=data) as mock_plans1_1: 
                with patch.object(facebook_proxy,'all_friends_names', return_value=['Mary']) as mock_names1_1:
                    ret1 = view_plans.available_plans(request1)
                    #the form in view_available_plans
                    template = loader.get_template('travelplans/view_plans.html')
                    context = RequestContext(request1, {
                        'plan_list': data,
                        'list_title': "All Available Plans",
                        'friend_list': ['Mary']
                    })
                    self.assertEqual(HttpResponse(template.render(context)).content, ret1.content)
                    
        request2 = HttpRequest()
        request2.user = self.user2            
        with patch.object(request2.user,'is_authenticated', return_value = False) as mock_auth1_2:            
            ret2 = view_plans.available_plans(request2)
            self.assertEqual(redirect('login').content, ret2.content)
        
        request3 = HttpRequest()
        request3.user = self.user1
        ret3 = view_plans.available_plans(request3)
        self.assertTrue('Return to Homepage' in ret3.content)
    

    def test_view_my_plans(self):
        request1 = HttpRequest()
        request1.user = self.user1
        
        data={'data':[
        {'id':self.plan1.id}
        ]}

        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth2_1:
            with patch.object(plan_manager.PlanManager,'get_plans_by_user', return_value=data) as mock_plans2_1:
                with patch.object(facebook_proxy, 'all_friends_names', return_value=['Gates']) as mock_names2_1:
                    ret1 = view_plans.my_plans(request1)
                    #the form in my_plans
                    template = loader.get_template('travelplans/view_plans.html')
                    context = RequestContext(request1, {
                        'plan_list': data,
                        'list_title': "All My Plans",
                        'friend_list': ['Gates']
                    })
                    self.assertEqual(HttpResponse(template.render(context)).content, ret1.content)
                    
        request2 = HttpRequest()
        request2.user = self.user2            
        with patch.object(request2.user,'is_authenticated', return_value = False) as mock_auth2_2:            
            ret2 = view_plans.my_plans(request2)
            self.assertEqual(redirect('login').content, ret2.content)
        
        request3 = HttpRequest()
        request3.user = self.user1
        ret3 = view_plans.my_plans(request3)
        self.assertTrue('Return to Homepage' in ret3.content)
           
    def test_view_joined_plans(self):
        request1 = HttpRequest()
        request1.user = self.user1
        
        data={'data':[
        {'id':self.plan1.id}
        ]}

        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth3_1:
            with patch.object(plan_manager.PlanManager,'get_joined_plans', return_value=data) as mock_plans3_1:
                with patch.object(facebook_proxy, 'all_friends_names', return_value=['Gates']) as mock_names3_1:
                    ret1 = view_plans.joined_plans(request1)
                    #the form in my_plans
                    template = loader.get_template('travelplans/view_plans.html')
                    context = RequestContext(request1, {
                        'plan_list': data,
                        'list_title': "All Joined Plans",
                        'friend_list': ['Gates']
                    })
                    self.assertEqual(HttpResponse(template.render(context)).content, ret1.content)
                    
        request2 = HttpRequest()
        request2.user = self.user2            
        with patch.object(request2.user,'is_authenticated', return_value = False) as mock_auth3_2:            
            ret2 = view_plans.joined_plans(request2)
            self.assertEqual(redirect('login').content, ret2.content)
        
        request3 = HttpRequest()
        request3.user = self.user1
        ret3 = view_plans.joined_plans(request3)
        self.assertTrue('Return to Homepage' in ret3.content)
        
        
    def test_view_plan_detail(self):
        request1 = HttpRequest()
        request1.user = self.user1
        '''
        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth:
            with patch.object(plan_manager.PlanManager,'get_plan_by_id', return_value=None) as mock_plans:
                #self.assertRaises(Exception,view_plans.view_plan_detail,request1, self.plan1.id)
                self.assertRaisesRegexp(Exception,'this plan do not exist',view_plans.view_plan_detail,request1, self.plan1.id)
        '''
        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth4_1:
            with patch.object(plan_manager.PlanManager,'get_plan_by_id', return_value=self.plan1) as mock_plans4_2:
                with patch.object(facebook_proxy, 'get_picture_url', return_value='') as mock_url4_1:
                    with patch.object(facebook_proxy, 'all_friends_names', return_value=['Gates']) as mock_names4_1:
                        ret1 = view_plans.view_plan_detail(request1, self.plan1.id)
                        #the form in my_plans
                        self.assertTrue(str(self.plan1.id) in ret1.content)
                    
        request2 = HttpRequest()
        request2.user = self.user2            
        with patch.object(request2.user,'is_authenticated', return_value = False) as mock_auth4_2:            
            ret2 = view_plans.view_plan_detail(request2, self.plan1.id)
            self.assertEqual(redirect('login').content, ret2.content)
        
        request3 = HttpRequest()
        request3.user = self.user1
        ret3 = view_plans.view_plan_detail(request3, self.plan1.id)
        self.assertTrue('Return to Homepage' in ret3.content)

        
    def test_help(self):
        request1 = HttpRequest()
        request1.user = self.user1
        ret1 = view_plans.help(request1)
        template = loader.get_template('travelplans/help.html')
        context = RequestContext(request1)
        self.assertEqual(HttpResponse(template.render(context)).content, ret1.content)
        
        
class JoinPlanTestCase(unittest.TestCase):


    def setUp(self):
        user1=User(username='John',is_superuser=0)
        social_auth1=UserSocialAuth(user_id=user1.id,uid='12345',provider='facebook',extra_data={'access_token':'1','id':'12345'})
        user1.save()
        user1.social_auth.add(social_auth1)
        user1.save()
        self.social_auth1=social_auth1
        self.user1=user1

        user2=User(username='Mary',is_superuser=0)
        self.user2=user2
        user2.save()

        user3=User(username='Mike',is_superuser=0)
        social_auth3=UserSocialAuth(user_id=user3.id,uid='facebookid3',provider='facebook',extra_data={'access_token':'3','id':'facebookid3'})
        user3.save()
        user3.social_auth.add(social_auth3)
        user3.save()
        self.user3=user3
        self.social_auth3=social_auth3

        plan1 = Plan(holder_id=user1.id, destination='newWorld', depart_time=datetime.date(2014, 12, 5), return_time=datetime.date(2014, 12, 6), limit = 3)
        plan1.save()
        self.plan1=plan1


    def tearDown(self):
        self.social_auth1.delete()
        self.user1.delete()
        self.user2.delete()
        self.social_auth3.delete()
        self.user3.delete()
        self.plan1.delete()


    def test_join_plan(self):
        request1 = HttpRequest()
        request1.user = self.user1
        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth:
            with patch.object(plan_manager.PlanManager,'joinable', return_value = True) as mock_join:
                with patch.object(JoinedPlan,'save', return_value = '') as mock_save:
                    ret1 = join_plan.join_plan(request1, self.plan1.id)
                    self.assertEqual(HttpResponse("true").content, ret1.content)
            #with patch.object(plan_manager.PlanManager,'joinable', return_value=False) as mock_join2:
                    #self.assertRaises(Exception, join_plan.join_plan, request1, self.plan1.id)
    
    def test_unjoin_plan(self):
        request1 = HttpRequest()
        request1.user = self.user1
        with patch.object(request1.user,'is_authenticated', return_value = True) as mock_auth:
            with patch.object(JoinedPlan.objects, 'get', return_value = '') as mock_jget:
                with patch.object(JoinedPlan, 'delete', return_value = '') as mock_del:
                    ret1 = join_plan.unjoin_plan(request1, self.plan1.id)
                    #self.assertEqual(HttpResponse("true").content, ret1.content)
        
        request2 = HttpRequest()
        request2.user = self.user2
        with patch.object(request2.user,'is_authenticated', return_value = False) as mock_auth2:            
            ret2 = join_plan.unjoin_plan(request2, self.plan1.id)
            self.assertEqual(redirect('login').content, ret2.content)
        
class SharePlanTestCase(unittest.TestCase):


    def setUp(self):
        user1=User(username='John',is_superuser=0)
        social_auth1=UserSocialAuth(user_id=user1.id,uid='12345',provider='facebook',extra_data={'access_token':'1','id':'12345'})
        user1.save()
        user1.social_auth.add(social_auth1)
        user1.save()
        self.social_auth1=social_auth1
        self.user1=user1

        user2=User(username='Mary',is_superuser=0)
        self.user2=user2
        user2.save()

        user3=User(username='Mike',is_superuser=0)
        social_auth3=UserSocialAuth(user_id=user3.id,uid='facebookid3',provider='facebook',extra_data={'access_token':'3','id':'facebookid3'})
        user3.save()
        user3.social_auth.add(social_auth3)
        user3.save()
        self.user3=user3
        self.social_auth3=social_auth3

        plan1 = Plan(holder_id=user1.id, destination='newWorld', depart_time=datetime.date(2014, 12, 5), return_time=datetime.date(2014, 12, 6), limit = 3)
        plan1.save()
        self.plan1=plan1


    def tearDown(self):
        self.social_auth1.delete()
        self.user1.delete()
        self.user2.delete()
        self.social_auth3.delete()
        self.user3.delete()
        self.plan1.delete()
        

    @mock.patch.object(facebook_proxy, 'share_plan_action', autospec=True)
    def test_share_plan(self, mock_share_plan_action):
        request1 = HttpRequest()
        request1.user = self.user1
        
        #with patch.object(request1.POST,'get', return_value = '') as mock_comment:
        share_plan.share_plan(request1, self.plan1.id)
        
        mock_share_plan_action.assert_called_with(self.user1, self.plan1, ''+" http://ajourney.co/travelplans/view_plan_detail/"+str(self.plan1.id)+"/")
        
class any(object):
    def __eq__(self, other):
        return True
        
        