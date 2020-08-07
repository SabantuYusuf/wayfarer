from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post
from django_fields import DefaultStaticImageField

class UserRegisterForm(UserCreationForm):
    prof_img = forms.ImageField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'city', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city']


class EditProfile(forms.ModelForm):
    city = forms.CharField()
    class Meta:
 	    model = User
 	    fields = ['first_name', 'last_name', 'city']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_img', 'title', 'content' )
        # fields = ('date', 'content', 'title', 'post_img')
        # add image and author to fields

