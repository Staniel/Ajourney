import facebook
import urllib2
import json
from travelplans.my_exception import FacebookError, DatabaseError

from social.apps.django_app.default.models import UserSocialAuth



def is_friend(current_user, possible_friend):
	if not current_user or not possible_friend:
		raise Exception('All users cannot be None!')
	friend_list = all_friends(current_user)
	if len(friend_list) > 0:
		social_possible_friend = possible_friend.social_auth.filter(provider='facebook').first()
		if social_possible_friend:
			if social_possible_friend.uid in friend_list:
				return True
	return False

    
def get_access_token(user):
	if user:
		social_user = user.social_auth.filter(provider='facebook',).first()
		token = social_user.extra_data['access_token']
		return token
	else:
		return None

        
def all_friends(user):

	friend_list = []
	if not user:
		raise Exception('User cannot be None!')
	try:
		token = get_access_token(user)
	except Exception as e:
		raise DatabaseError(e.message)
	try:
		graph=facebook.GraphAPI(token)
		friends_response = graph.get_object('/me/friends')
		friends = friends_response['data']
		for friend in friends:
			friend_list.append(friend['id'])
	except Exception as e:
		raise FacebookError(e.message)
	return friend_list


def share_plan_action(user, plan, comment):
	try:
		token = get_access_token(user)
	except Exception as e:
		raise DatabaseError(e.message)
	try:
		graph = facebook.GraphAPI(token)
		graph.put_object('me', 'feed', message=comment)
		return True
	except Exception as e:
		raise FacebookError(e.message)


def get_picture_url(holder_id):
	try:
		# the following is the api call version of the get_picture_url
		# graph = facebook.GraphAPI(social_current_user.extra_data['access_token'])
		# profile = graph.get_object('/'+str(holder_id)+'/picture?type=large')
		# user_picture_url = profile['url']
		# return user_picture_url
		if UserSocialAuth.objects.get(uid__exact=holder_id):  # pragma: no branch
			user_picture_url = 'http://graph.facebook.com/'+str(holder_id)+'/picture?type=large'
			return user_picture_url		
	except UserSocialAuth.DoesNotExist:
		raise Exception('User has not used our website!')