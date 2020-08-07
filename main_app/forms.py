from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class UserRegisterForm(UserCreationForm):
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
 	class Meta:
 		model = User
 		fields = ['first_name', 'last_name']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'title', 'city_options']
        # add image and author to fields

