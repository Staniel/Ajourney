import facebook
import urllib2
import json

class FBuser:
    def __init__(self, FBid, name):
        self.id = FBid
        self.name = name


def is_friend(user_a, user_b):
	social_user_b = user_b.social_auth.filter( provider='facebook',).first()
	if social_user_b:
		graph = facebook.GraphAPI(social_user_b.extra_data['access_token'])
		profile_b = graph.get_object("me")
		user_b_facebookid = profile_b['id']
		if user_b_facebookid in all_friends(user_a):
			return True
	return False

def all_friends(user):
	friend_list=[]
	social_user = user.social_auth.filter( provider='facebook',).first()
	if social_user:
		url = u'https://graph.facebook.com/{0}/' \
            u'friends?fields=id,name,location,picture' \
            u'&access_token={1}'.format(social_user.uid,
        social_user.extra_data['access_token'],)
        response = urllib2.Request(url) 
    	friends_json = json.loads(urllib2.urlopen(response).read()).get('data')   
    	for i in xrange(len(friends_json)):
			friend_list.append(friends_json[i]['id'])
	return friend_list

def share_plan(user, plan, comment):
    social_user = user.social_auth.filter( provider='facebook',).first()
    graph = facebook.GraphAPI(social_user.extra_data['access_token'])
    graph.put_object('me', 'feed', message = comment)
    return True