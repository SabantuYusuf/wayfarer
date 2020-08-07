from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

# Create your Models here.

# Post Model
class Post(models.Model):
    # image = Image.open('../static/images/stickynote.png') 
    post_img = models.ImageField(upload_to='images/', default='stickynote.png')
    content = models.CharField("Content", max_length=250, blank=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField("Title", max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# add actual city

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField("Current City", max_length=85, blank=True)
    prof_img = models.ImageField("Profile Image", null=True, blank=True, upload_to='images/', default='defaultpic.png')

# City Model
class City(models.Model):
	name = models.CharField(max_length=100)
	# image = models.ImageField() 