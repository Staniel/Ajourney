from django.contrib.auth.models import User

def get_by_username(user_name):
	try:
		user=User.objects.get(username__exact=user_name)
		return user
	except:
		return None

