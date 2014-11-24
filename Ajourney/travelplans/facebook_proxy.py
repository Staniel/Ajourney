import facebook
import urllib2
import json
from travelplans.my_exception import FacebookError, DatabaseError


class FBuser:
    def __init__(self, FBid, name):
        self.id = FBid
        self.name = name


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


def all_friends(user):
    friend_list = []
    try:
        social_user = user.social_auth.filter(provider='facebook',).first()
    except DatabaseError as db_e:
        raise db_e
    if social_user:
        url = u'https://graph.facebook.com/{0}/'\
            u'friends?fields=id,name,location,picture'\
            u'&access_token={1}'.format(social_user.uid,
            social_user.extra_data['access_token'],)
        try:
            response = urllib2.Request(url)
            friends_json = json.loads(urllib2.urlopen(response).read()).get('data')
            for friend_json in friends_json:
                friend_list.append(friend_json['id'])
        except FacebookError as fb_e:
            raise fb_e
    return friend_list


def share_plan_action(user, plan, comment):
    try:
        social_user = user.social_auth.filter(provider='facebook',).first()
    except DatabaseError as db_e:
        raise db_e
    try:
        graph = facebook.GraphAPI(social_user.extra_data['access_token'])
        graph.put_object('me', 'feed', message=comment)
        return True
    except FacebookError as fb_e:
        raise fb_e


def get_picture_url(current_user, holder_id):
    try:
        social_current_user = current_user.social_auth.filter(provider='facebook',).first()
    except DatabaseError as db_e:
        raise db_e
    try:
        if social_current_user:
            # the following is the api call version of the get_picture_url
            # graph = facebook.GraphAPI(social_current_user.extra_data['access_token'])
            # profile = graph.get_object('/'+str(holder_id)+'/picture?type=large')
            # user_picture_url = profile['url']
            # return user_picture_url

            user_picture_url = 'http://graph.facebook.com/'+str(holder_id)+'/picture?type=large'
            return user_picture_url
        else:
            return ''
    except FacebookError as fb_e:
        raise fb_e
