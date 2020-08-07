from django.shortcuts import render, redirect
from .models import Profile, Post, City
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login
from .forms import UserRegisterForm, ProfileRegisterForm, EditProfile, PostForm, EditProfileCity


# Create your views here.

# Home
def home(request):
	return render(request, 'home.html')

# USER ROUTES

# About
def about(request):
  return render(request, 'about.html')


# Sign Up
def signup(request):
  error_message = ''
  prof_form = UserRegisterForm(request.POST, request.FILES)
  p_reg_form = ProfileRegisterForm(request.POST, request.FILES)
  if request.method == 'POST':
    if prof_form.is_valid() and p_reg_form.is_valid():
      user = prof_form.save()
      profile = p_reg_form.save(commit=False)
      profile.user = user
      profile.save()
      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'
      prof_form = UserRegisterForm()
      p_reg_form = ProfileRegisterForm()
  context = {
    'prof_form': prof_form, 
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
  if request.method == 'GET':
    Profiles = Profile.objects.all()
    return render(request, 'users/profile.html', context)

# Edit Profile
@login_required
def edit_profile(request):
  user = request.user
  current_profile = Profile.objects.get(user=user)
  if request.method == 'POST':
    # print("This is the thing ", request.POST['prof_img'])
    e_form = EditProfile(request.POST, request.FILES, instance=user)
    p_form = ProfileRegisterForm(request.POST, request.FILES, instance=current_profile)
    
    if e_form.is_valid() and p_form.is_valid():
      user = e_form.save()
      print(f"USER {user}")
      profile = p_form.save(commit=False)
      profile.save() 
      login(request, user)
      return redirect('profile')
  else:
    e_form = EditProfile(instance=user)
    p_form = ProfileRegisterForm( instance=current_profile)
  context = {
    'e_form': e_form, 
    'p_form': p_form,
  }
  return render(request, 'users/edit.html', context)

# POST ROUTES

# Create (New) Post Route
@login_required
def new_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST, request.FILES)
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
  if request.method == 'GET':
    Posts = Post.objects.all()
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
# CAN WE ADD A POP UP INSTEAD OF REDIRECTING? (NEED TO ADD ERROR MESSAGE
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






# def sanfran_new(request):
#     if request.method == 'POST':
#       post= PostForm(request.POST, request.FILES)
#     if post_form.is_valid():
#     # image = request.POST['image']
#       new_post = post_form.save(commit=False)
#       # user = Profile.ojects.get(user_id=user_id)
#       new_post.user = request.user
#       new_post.save()

#       # return redirect('profile', new_post.id)
#       return redirect('cities', new_post.id)
#     else:
#       post = PostForm()
#       return render(request, 'posts2/new.html', {'post_form': post_form})




# Credit = image upload = https://www.geeksforgeeks.org/python-uploading-images-in-django/
# downloaded paperclip and pillow


