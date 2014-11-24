from django.utils import unittest
from travelplans import facebook_proxy
from mock import patch
import urllib2
from social.apps.django_app.default.models import UserSocialAuth
from travelplans.models import User,Plan
import json
import facebook
from travelplans.my_exception import FacebookError, DatabaseError
import mock
import datetime



class FacebookProxyTestCase(unittest.TestCase):

    def setUp(self):
        user1=User(username='user1',is_superuser=0)
        social_auth1=UserSocialAuth(user_id=user1.id,uid='12345',provider='facebook',extra_data={'access_token':'1','id':'12345'})
        user1.save()
        user1.social_auth.add(social_auth1)
        user1.save()
        self.social_auth1=social_auth1
        self.user1=user1

        user2=User(username='user2',is_superuser=0)
        self.user2=user2
        user2.save()

        user3=User(username='user3',is_superuser=0)
        self.user3=user3
        social_auth3=UserSocialAuth(user_id=user3.id,uid='facebookid3',provider='facebook',extra_data={'access_token':'3','id':'facebookid3'})
        user3.save()
        user3.social_auth.add(social_auth3)
        self.social_auth3=social_auth3

        user4=User(username='user4',is_superuser=0)
        social_auth4=UserSocialAuth(user_id=user4.id,uid='facebookid4',provider='facebook',extra_data={'access_token':'4','id':'facebookid4'})
        user4.save()
        user4.social_auth.add(social_auth4)
        user1.save()
        self.social_auth4=social_auth4
        self.user4=user4

        user5=User(username='user5',is_superuser=0)
        social_auth5=UserSocialAuth(user_id=user5.id,uid='facebookid5',provider='facebook',extra_data={'access_token':'5','id':'facebookid5'})
        user5.save()
        user5.social_auth.add(social_auth5)
        user5.save()
        self.social_auth5=social_auth5
        self.user5=user5

        plan1 = Plan(holder_id=user1.id, destination='newWorld', depart_time=datetime.date(2014, 12, 5), return_time=datetime.date(2014, 12, 6), limit = 3)
        plan1.save()
        self.plan1=plan1



    def tearDown(self):
        self.social_auth1.delete()
        self.user1.delete()
        self.user2.delete()
        self.social_auth3.delete()
        self.user3.delete()
        self.social_auth4.delete()
        self.user4.delete()
        self.social_auth5.delete()
        self.user5.delete()
        self.plan1.delete()
        

    def test_all_friends(self):
        data={'data':[
        {'id':'facebookid1'},
        {'id':'facebookid2'}
        ]}
        with patch.object(facebook.GraphAPI,'get_object', return_value=data) as mock_method:
            friend_list=facebook_proxy.all_friends(self.user1)
            self.assertEqual(friend_list,['facebookid1','facebookid2'])

        self.assertRaisesRegexp(Exception,'User cannot be None!',facebook_proxy.all_friends,None)

        self.assertRaises(DatabaseError,facebook_proxy.all_friends,self.user2)

        with patch.object(facebook.GraphAPI,'get_object',side_effect='Exception') as mock_method:
            self.assertRaises(FacebookError,facebook_proxy.all_friends,self.user1)

       
    def test_is_friend(self):
        data=['facebookid4']
        self.assertRaisesRegexp(Exception,'All users cannot be None!',facebook_proxy.is_friend,None,self.user1)
        self.assertRaisesRegexp(Exception,'All users cannot be None!',facebook_proxy.is_friend,self.user1,None)

        with patch.object(facebook_proxy,'all_friends', return_value=data) as mock_method:
            result1=facebook_proxy.is_friend(self.user1,self.user4)
            result2=facebook_proxy.is_friend(self.user1,self.user5)
            self.assertTrue(result1)
            self.assertFalse(result2)
        with patch.object(facebook_proxy,'all_friends', return_value=[]) as mock_method:
            self.assertFalse(facebook_proxy.is_friend(self.user1,self.user4))

        with patch.object(facebook_proxy,'all_friends', return_value=data) as mock_method:
            self.assertFalse(facebook_proxy.is_friend(self.user1,self.user2))
       

    def test_get_picture_url(self):
        result1=facebook_proxy.get_picture_url(self.user1.social_auth.filter(provider='facebook').first().uid)
        try:
            response = urllib2.Request(result1)
            urllib2.urlopen(response).read()
            self.assertTrue(True)
        except urllib2.HTTPError as e:
            self.assertTrue(False)

        self.assertRaisesRegexp(Exception,'User has not used our website',facebook_proxy.get_picture_url,'123456')

    @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
    def test_share_plan_action(self, mock_put_object):
        facebook_proxy.share_plan_action(self.user1, self.plan1, 'test')
        #verify
        mock_put_object.assert_called_with(any(), 'me', 'feed',message='test')



    def test_share_plan_action_db_fails(self):
        self.assertRaises(DatabaseError, facebook_proxy.share_plan_action, self.user2, self.plan1, 'test')    


    def test_share_plan_action_fb_fails(self):
        self.assertRaises(FacebookError, facebook_proxy.share_plan_action, self.user1, self.plan1, 'test')

    def test_get_access_token(self):
        token=facebook_proxy.get_access_token(self.user1)
        self.assertEqual(token,'1')
        token=facebook_proxy.get_access_token(None)
        self.assertEqual(token,None)

class any(object):
    def __eq__(self, other):
        return True

    '''
    def test_test2(self):
         with patch.object(urllib2, 'Request', return_value=1) as mock_method:
            result=facebook_proxy.test2()
            self.assertEqual(result,1)
    '''