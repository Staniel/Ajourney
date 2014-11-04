from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Plan(models.Model):
	holder = models.ForeignKey(User)
	description = models.CharField(max_length=500)
	destination = models.CharField(max_length=200)
	limit = models.IntegerField()
	depart_time = models.DateTimeField()
	return_time = models.DateTimeField()
	def __str__(self):
		return self.description
