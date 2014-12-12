import facebook
import urllib2
import json

class FBuser:
    def __init__(self, FBid, name):
        self.id = FBid
        self.name = name

def is_friend(user_a,user_b):
    if not user_a or not user_b:
        return False
    friend_list=all_friends(user_a)
    if len(friend_list)>0:
        social_user_b = user_b.social_auth.filter(provider = 'facebook').first()
        if social_user_b:
            if social_user_b.uid in friend_list:
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
    	for friend_json in friends_json:
            friend_list.append(friend_json['id'])
	return friend_list
def all_friends_names(user):
    friend_list=[]
    social_user = user.social_auth.filter( provider='facebook',).first()
    if social_user:
        url = u'https://graph.facebook.com/{0}/' \
            u'friends?fields=id,name,location,picture' \
            u'&access_token={1}'.format(social_user.uid,
        social_user.extra_data['access_token'],)
        response = urllib2.Request(url) 
        friends_json = json.loads(urllib2.urlopen(response).read()).get('data')   
        for friend_json in friends_json:
            friend_list.append(friend_json)
    return friend_list

def share_plan_action(user, plan, comment):
    try:
    	social_user = user.social_auth.filter( provider='facebook',).first()
    	graph = facebook.GraphAPI(social_user.extra_data['access_token'])
    	graph.put_object('me', 'feed', message = comment)
    	return True
    except Exception as e:
    	raise e

def get_picture_url(user, holder_id):
    social_user = user.social_auth.filter( provider='facebook',).first()
    try:
        if social_user:
        #for server only don't know why if use facebook GraphAPI the ?type=large is not work, so I return the id of holder and by id get the profile
            '''
            graph = facebook.GraphAPI(social_user.extra_data['access_token'])
            profile = graph.get_object('/'+str(holder_id)+'/picture?type=large')
            user_picture_url = profile['url']
            return user_picture_url
            '''
            user_picture_url = 'http://graph.facebook.com/'+str(holder_id)+'/picture?type=large'
            return user_picture_url
        else:
            return ''
    except Exception as e:
        print e.message
             