from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your Models here.

# Profile model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# user.first_name = first_name
	# user.last_name = last_name
	# user.date_joined = date_joined
	# city = models.CharField('City', max_length=100)
	# date = models.DateField('join date')
	
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
	
	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

# class User(models.Model):
# 	first_name = models.CharField(max_length=50)
# 	last_name = models.CharField(max_length=50)
# 	username = models.CharField(max_length=50)
# 	password = models.CharField(max_length=50)
# 	date_joined = models.DateField()


# Post Model
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=250)
	# add city and author

# City Model
class City(models.Model):
	name = models.CharField(max_length=100)
	# image = models.ImageField() 
	# install pillow



