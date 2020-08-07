from django.shortcuts import render, redirect
from .models import Profile, Post, City
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login
from .forms import UserRegisterForm, ProfileRegisterForm, EditProfile, PostForm


# HOME
def home(request):
	return render(request, 'home.html')

# USER ROUTES

# Sign Up
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
      return redirect('profile')
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
def profile(request):
  user = request.user
  print(user)
  current_user = Profile.objects.get(user=user)
  posts = Post.objects.filter(user=user)
  print(f"current_user {current_user}")
  context = {
    'profile': current_user,
    'posts': posts
  }
  return render(request, 'users/profile.html', context)

# Edit Profile
@login_required
def edit_profile(request):
  user = request.user
  current_profile = Profile.objects.get(user=user)

  if request.method == 'POST':
    form = EditProfile(request.POST, instance=user)
    p_form = ProfileRegisterForm(request.POST, instance=current_profile)
    if form.is_valid() and p_form.is_valid():
      user = form.save()
      print(f"USER {user}")
      profile = p_form.save()
      login(request, user)
      return redirect('profile')
  else:
    form = EditProfile(instance=user)
    p_form = ProfileRegisterForm( instance=current_profile)
  return render(request, 'users/edit.html', {'form': form, 'p_form': p_form})


# POST ROUTES

# Create (New) Post Route
@login_required
def new_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save(commit=False)
      new_post.user = request.user
      new_post.city_id = request.POST['city_options']
      new_post.save()
      return redirect('post', new_post.id)
  else:
    post_form = PostForm()
    return render(request, 'posts2/new.html', {'post_form': post_form})

# Post Show Page
def post(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {
    'post': post
  }
  print(post)
  return render(request, 'posts2/postsshow.html', context)

# Delete Post
@login_required
def delete_post(request, post_id):
  error_message = ''
  post = Post.objects.get(id=post_id)
  if request.user == post.user:
    Post.objects.filter(id=post_id).delete()
    return redirect('profile')
  else:
    error_message = 'You can only delete your own post'
    context = {
      'error': error_message
    }  
    return render(request, 'cities/citydefault.html', context)
# CAN WE ADD A POP UP INSTEAD OF REDIRECTING? (NEED TO ADD ERROR MESSAGE)




  # Post.objects.get(id=post_id).delete()
  # return redirect('profile')



# CITY ROUTES

def cities(request):
	return render(request, 'cities/citydefault.html')

def london(request):
  posts = Post.objects.filter(city_id='3').order_by('-date')
  print(posts)
  context = {
    'posts': posts
  }
  return render(request, 'cities/london.html', context)

def sanfran(request):
  posts = Post.objects.filter(city_id='1').order_by('-date')
  print(posts)
  context = {
    'posts': posts
  }
  return render(request, 'cities/sanfran.html', context)

def seattle(request):
  posts = Post.objects.filter(city_id='2').order_by('-date')
  print(posts)
  context = {
    'posts': posts
  }
  return render(request, 'cities/seattle.html', context)

def sydney(request):
  posts = Post.objects.filter(city_id='4').order_by('-date')
  print(posts)
  context = {
    'posts': posts
  }
  return render(request, 'cities/sydney.html', context)

