from django.db import models
from django.contrib.auth.models import User

# Create your Models here.

# Profile model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField("City", max_length=85, blank=True)
	
# Post Model
class Post(models.Model):
    # image = models.ImageField()
    content = models.CharField("Content", max_length=250, blank=True)
    date = models.DateField()
    title = models.CharField("Title", max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# add actual city and author

# City Model
class City(models.Model):
	name = models.CharField(max_length=100)
	# image = models.ImageField() 
	# install pillow



