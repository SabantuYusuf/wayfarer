from django.shortcuts import render, redirect
from .models import Profile, Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login
from .forms import UserRegisterForm, ProfileRegisterForm


# Create your views here.

# Temp data

# posts = [
#   Post('Big Ben got Booty', 'Some Guy', 'Dang BB is huge and keeps correct time? You go, Ben Coco!', 'London'),
#   Post('Tour Busses - Watch Your Head!', 'Guy #2', 'Hit my head going under a tree. 2/10', 'London'),
#   Post('Phone Booths Still Exist?', 'Some Girl!', 'Did not know these still existed. Went in one to make a call and realized it was disconnected', 'London'),
# ]
  


def home(request):
	return render(request, 'home.html')

# User Routes
def signup(request):
  error_message = ''
  form = UserRegisterForm(request.POST)
  p_reg_form = ProfileRegisterForm(request.POST)
  if request.method == 'POST':
    if form.is_valid() and p_reg_form.is_valid():
      user = form.save()

      profile = p_reg_form.save(commit=False)
      profile.user = user
      profile.save()

      login(request, user)
      return redirect('profile', user.id)
    else:
      error_message = 'Invalid sign up - try again'
      form = UserRegisterForm()
      p_reg_form = ProfileRegisterForm()
  context = {
    'form': form, 
    'p_reg_form': p_reg_form,
    'error_message': error_message,
  }
  return render(request, 'registration/signup.html', context)

# Profile
def profile(request, user_id):
  current_user = User.objects.get(id=user_id)
#   print(current_user.date_joined)
  context = {
    'profile': current_user,
  }
  return render(request, 'users/profile.html', context)


# City Route
def cities(request):
	return render(request, 'cities.html')
