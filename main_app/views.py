from django.shortcuts import render, redirect
from .models import Profile, Post
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

# User Routes-----

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
      # return redirect('profile', user.id)
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
# def profile(request, user_id):
def profile(request):
  # print(f"user_id {user_id}")
  # current_user = Profile.objects.all().filter(username=request.user)
  # current_user = Profile.objects.get(user=user_id)
  user = request.user
  print(user)
  current_user = Profile.objects.get(user=user)
  posts = Post.objects.filter(user=user)
  print(f"current_user {current_user}")
#   print(current_user.date_joined)

  context = {
    'profile': current_user,
    'posts': posts
  }
  if request.method == 'GET':
    Profiles = Profile.objects.all()
    return render(request, 'users/profile.html', context)

# Edit Profile
# def edit_profile(request, user_id):
def edit_profile(request):
  # current_profile = Profile.objects.get(user=user_id)
  user = request.user
  current_profile = Profile.objects.get(user=user)

  if request.method == 'POST':
    # print("This is the thing ", request.POST['prof_img'])
    form = EditProfile(request.POST, request.FILES, instance=user)
    p_form = ProfileRegisterForm(request.POST, request.FILES, instance=current_profile)
    
    if form.is_valid() and p_form.is_valid():
      user = form.save()
      print(f"USER {user}")
      profile = p_form.save(commit=False)
      profile.save()
   
      login(request, user)
      return redirect('profile')
  else:
    form = EditProfile(instance=user)
    p_form = ProfileRegisterForm( instance=current_profile)
  context = {
    'form': form, 
    'p_form': p_form,
  }
  return render(request, 'users/edit.html', context)


# Post Routes------

# Create (New) Post Route
def new_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
    # image = request.POST['image']
      new_post = post_form.save(commit=False)
      # user = Profile.ojects.get(user_id=user_id)
      new_post.user = request.user
      new_post.save()

      # return redirect('profile', new_post.id)
      return redirect('post', new_post.id)
  else:
    post_form = PostForm()
    return render(request, 'posts2/new.html', {'post_form': post_form})
    # , {'new_post': Posts}

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
def delete_post(request, post_id):
  Post.objects.get(id=post_id).delete()
  return redirect('profile')
  #works, but edit code to redirect to profile



# City Routes-----

def cities(request):
	return render(request, 'cities/citydefault.html')

def london(request):
  return render(request, 'cities/london.html')


def sanfran(request):
      return render(request, 'cities/sanfran.html')

def seattle(request):
  return render(request, 'cities/seattle.html')

def sydney(request):
  return render(request, 'cities/sydney.html')




# Edit Profile
# def edit_profile(request, user_id):
def edit_profile(request):
  # current_profile = Profile.objects.get(user=user_id)
  user = request.user
  current_profile = Profile.objects.get(user=user)

  if request.method == 'POST':
    form = EditProfile(request.POST, instance=user)
    # print(form)
    p_form = ProfileRegisterForm(request.POST, instance=current_profile)
    # print(p_form)
    if form.is_valid() and p_form.is_valid():
      user = form.save()
      print(f"USER {user}")
      profile = p_form.save()

      # profile.user = user
      
      # print(f"PROFILE.USER {profile.user}")

      # profile.save()
      # user.id = current_profile.id
      # return redirect('profile', profile.user.id)
      login(request, user)
      return redirect('profile')
  else:
    form = EditProfile(instance=user)
    p_form = ProfileRegisterForm( instance=current_profile)
  return render(request, 'users/edit.html', {'form': form, 'p_form': p_form})



# Credit = image upload = https://www.geeksforgeeks.org/python-uploading-images-in-django/
# downloaded paperclip and pillow

