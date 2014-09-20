from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.core.files import File
from PIL import Image
import base64


# Create your models here.
class user(models.Model):
	user = models.OneToOneField(User)
	uname = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	uid = models.CharField(max_length=50,unique = True)
	mobile = models.CharField(max_length=30)
	uaddr = models.CharField(max_length=100)

class book(models.Model):
	btitle = models.CharField(max_length=50)
	category = models.CharField(max_length=50)	
	author = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	bid = models.CharField(max_length=20,unique = True)
	quantity = models.IntegerField(max_length=50)

class booklend(models.Model):
	user = models.ForeignKey('user')	
	book = models.ForeignKey('book')
	status = models.CharField(max_length=50)			
	doi = models.DateTimeField(max_length=50)
	dor = models.DateTimeField(max_length=50)


class Family(models.Model):	
	ration_card = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	code = models.IntegerField(max_length=50)

class FamilyMember(models.Model):
	name = models.CharField(max_length=50)
	personcode = models.CharField(max_length=50)
	family = models.ForeignKey('Family')
	Gender = models.CharField(max_length=50)
	maritalstatus = models.CharField(max_length=50,null=True)	
	Age = models.IntegerField(max_length=50)
	qualification = models.CharField(max_length=50)
	occupation = models.CharField(max_length=50)
	income = models.CharField(max_length=50,null=True)	
	IsStudent = models.BooleanField(default=False)
	standard = models.CharField(max_length=50, null=True, blank=True)
	institution = models.CharField(max_length=50, null=True, blank=True)
	grade = models.CharField(max_length=50, null=True, blank=True)

class Class(models.Model):
	subject = models.CharField(max_length=50)
	
class StudentClass(models.Model):
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember', null=True, blank=True)

class Attendance(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember')
	attendance = models.BooleanField(default=False)
	date = models.CharField(max_length=11, default=Date)
			
class Event(models.Model):
	name = models.CharField(max_length=50)

class EventData(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	event = models.ForeignKey('Event')
	family = models.ForeignKey('Family')
	date = models.CharField(max_length=11, default=Date)



