<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

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
=======
# from django import forms
# from .models import Profile, Post, City
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#     name = forms.CharField()

#     class Meta:
#         model = User
#         fields = ('username', 'name', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.extra_field = self.cleaned_data["extra_field"]
#         if commit:
#             user.save()
#         return user

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('city')
>>>>>>> submaster
