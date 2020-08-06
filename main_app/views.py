from django.shortcuts import render, redirect
from .models import Profile, Post
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login
<<<<<<< HEAD
from .forms import UserRegisterForm, ProfileRegisterForm, EditProfile

=======
from .forms import UserRegisterForm, ProfileRegisterForm, PostForm
>>>>>>> submaster


# Create your views here.

# Temp data
# class Post:
#   def __init__(self, title, author, content, city):
#     self.title = title
#     self.author = author
#     self.content = content
#     self.city = city

# posts = [
#   Post('Big Ben got Booty', 'Some Guy', 'Dang BB is huge and keeps correct time? You go, Ben Coco!', 'London'),
#   Post('Tour Busses - Watch Your Head!', 'Guy #2', 'Hit my head going under a tree. 2/10', 'London'),
#   Post('Phone Booths Still Exist?', 'Some Girl!', 'Did not know these still existed. Went in one to make a call and realized it was disconnected', 'London'),
# ]

# Home
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
      # return redirect('profile', user.id)
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
<<<<<<< HEAD
# def profile(request, user_id):
def profile(request):
  # print(f"user_id {user_id}")
  # current_user = Profile.objects.all().filter(username=request.user)
  # current_user = Profile.objects.get(user=user_id)
  user = request.user
  print(user)
  current_user = Profile.objects.get(user=user)
  print(f"current_user {current_user}")
#   print(current_user.date_joined)
=======
# def profile(request, user_id, #post_id):
def profile(request, user_id):
  current_user = Profile.objects.get(user=user_id)
  posts = Post.objects.filter(user=request.user)
  print(posts)
>>>>>>> submaster
  context = {
    'profile': current_user,
    'posts': posts
  }
  return render(request, 'users/profile.html', context)


# Create (New) Post Route
def new_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
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

# Post Show Page
def post(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {
    'post': post
  }
  print(post)
  return render(request, 'posts2/postsshow.html', context)

# Post Index Page (Delete Later - Just for Testing)
# def post(request):
#   posts = Post.objects.filter(user=request.user)
#   context = {
#     'posts': posts
#   }
#   return render(request, 'users/profile.html', context)

# Add Posts Route
# def assoc_posts(request, user_id, post_id):
#   user = Profile.objects.get(user=user_id)
#   post = Post.objects.get(id=post_id)
#   user.posts.add(post)
#   return redirect('profile', user_id)


# City Routes
def cities(request):
	return render(request, 'cities.html')


def london(request):
  return render(request, 'cities/london.html')

<<<<<<< HEAD
# Edit Profile
# def edit_profile(request, user_id):
def edit_profile(request):
  # current_profile = Profile.objects.get(user=user_id)
  user = request.user
  current_profile = Profile.objects.get(user=user)
=======

# Edit Profile
def edit_profile(request, user_id):
  current_profile = Profile.objects.get(user=user_id)
>>>>>>> submaster
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


