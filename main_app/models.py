from django.db import models
from django.contrib.auth.models import User

# Create your Models here.

# Profile model
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=100)
	date = models.DateField('join date')

# Post Model
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=250)

# City Model
class City(models.Model):
	name = models.CharField(max_length=100)
	# image = models.ImageField() 
	# install pillow



