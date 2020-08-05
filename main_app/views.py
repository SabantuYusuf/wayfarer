from django.shortcuts import render, redirect
from .models import Profile, Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


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
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('profile', user_id)
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Profile
def profile(request, user_id):
  user = User.objects.get(id=user_id)
  context = {
    'user': User
  }
  return render(request, 'users/profile.html', context)


# City Route
def cities(request):
	return render(request, 'cities.html')
