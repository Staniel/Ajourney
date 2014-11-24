import facebook
import urllib2
import json


def is_friend(current_user,possible_friend):
    if not current_user or not possible_friend:
        return False
    friend_list=all_friends(current_user)
    if len(friend_list)>0:
        social_possible_friend = possible_friend.social_auth.filter(provider = 'facebook').first()
        if social_possible_friend:
            if social_possible_friend.uid in friend_list:
                return True
    return False

def all_friends(user):
	friend_list=[]
	social_user = user.social_auth.filter( provider='facebook',).first()
	if social_user:
        try:
    		url = u'https://graph.facebook.com/{0}/' \
                u'friends?fields=id,name,location,picture' \
                u'&access_token={1}'.format(social_user.uid,
            social_user.extra_data['access_token'],)
            response = urllib2.Request(url) 
        	friends_json = json.loads(urllib2.urlopen(response).read()).get('data')   
        	for i in xrange(len(friends_json)):
    			friend_list.append(friends_json[i]['id'])
        except Exception as e:
            raise e
	return friend_list

def share_plan_action(user, plan, comment):
    try:
    	social_user = user.social_auth.filter( provider='facebook',).first()
    	graph = facebook.GraphAPI(social_user.extra_data['access_token'])
    	graph.put_object('me', 'feed', message = comment)
    	return True
    except Exception as e:
    	raise e

def get_picture_url(current_user):
    social_current_user = current_user.social_auth.filter( provider='facebook',).first()
    try:
        if social_current_user:
            graph = facebook.GraphAPI(social_current_user.extra_data['access_token'])
            profile = graph.get_object('/me/picture')
            user_picture_url = profile['url']
            return user_picture_url
        else:
            return ''
    except Exception as e:
        raise e
