from django.db import models
from datetime import date
from django.core.files import File
from PIL import Image
import base64




class Family(models.Model):	
	ration_card = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	code = models.IntegerField(max_length=50)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.ration_card
	def __unicode__(self):
		return self.city
	def __unicode__(self):
		return self.street
	def __unicode__(self):
		return self.code	

class FamilyMember(models.Model):
	name = models.CharField(max_length=50)
	personcode = models.CharField(max_length=50)
	family = models.ForeignKey('Family')
	Gender = models.CharField(max_length=50)
	Age = models.IntegerField(max_length=50)
	qualification = models.CharField(max_length=50)
	occupation = models.CharField(max_length=50)
	IsStudent = models.BooleanField(default=False)
	standard = models.CharField(max_length=50, null=True, blank=True)
	institution = models.CharField(max_length=50, null=True, blank=True)
	grade = models.CharField(max_length=50, null=True, blank=True)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.name
	def __unicode__(self):
		return self.personcode
	def __unicode__(self):
		return self.family
	def __unicode__(self):
		return self.Gender
	def __unicode__(self):
		return self.Age
	def __unicode__(self):
		return self.qualification
	def __unicode__(self):
		return self.occupation
	def __unicode__(self):
		return self.IsStudent
	def __unicode__(self):
		return self.standard
	def __unicode__(self):
		return self.institution
	def __unicode__(self):
		return self.grade

class Class(models.Model):
	subject = models.CharField(max_length=50)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.subject
	
class StudentClass(models.Model):
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember', null=True, blank=True)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.classname
	def __unicode__(self):
		return self.student

class Attendance(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember')
	attendance = models.BooleanField(default=False)
	date = models.CharField(max_length=11, default=Date)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.classname
	def __unicode__(self):
		return self.student
	def __unicode__(self):
		return self.attendance
	def __unicode__(self):
		return self.date
			
class Event(models.Model):
	name = models.CharField(max_length=50)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.name

class EventData(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	event = models.ForeignKey('Event')
	family = models.ForeignKey('Family')
	date = models.CharField(max_length=11, default=Date)

	class Meta: 
		app_label = 'valuation'

	def __unicode__(self):
		return self.event
	def __unicode__(self):
		return self.family
	def __unicode__(self):
		return self.date


	
# class CachedImage(models.Model):
#     url = models.CharField(max_length=255, unique=True)
#     photo = models.ImageField(upload_to='/home/smathik/family/gallery', blank=True)

# class Category(models.Model):
 

# 	class Album(models.Model):   
#     	category = models.ForeignKey(Category, related_name='albums')

# class Image(models.Model):
#     album = models.ForeignKey(Album)
    # image = models.ImageField(upload_to = 'home/smathik/family/gallery')