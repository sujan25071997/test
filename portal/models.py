from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone

class UserProfile(models.Model):
	users = models.OneToOneField(User, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.users

class Trainers(models.Model):
	name = models.CharField(max_length=40)
	expertis = models.CharField(max_length=40)
	date = models.DateField(null=True)

	def __str__(self):
		return self.name

class Courses(models.Model):
	name= models.CharField(max_length= 40)
	duration=models.IntegerField()
	fees = models.IntegerField()
	trainer = models.ForeignKey(Trainers, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.name

class Students_Profile(models.Model):
	user_id = models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	email = models.EmailField(max_length=255, unique=True)
	course = models.ManyToManyField(Courses)
	trainer =  models.ForeignKey(Trainers, on_delete=models.CASCADE)
	enrolled_date = models.DateField(null=True)
	completion_date = models.DateField(null=True)
	paid_amount = models.IntegerField(null=True)

	def __str__(self):
		return self.name

class Payment(models.Model):
	course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
	amount = models.IntegerField()
	method = models.CharField(max_length=64)
	note = models.CharField(max_length=256)
	date = models.DateField(null=True)

	def __str__(self):
		return self.amount
