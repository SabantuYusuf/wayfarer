from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
<<<<<<< HEAD
	path('about', views.about, name='about'),
=======

>>>>>>> submaster
	# User Routes---

<<<<<<< HEAD
=======
	# Sign Up
	path('accounts/signup/', views.signup, name='signup'),
>>>>>>> 39c0e53ac810d87fc9d749080fe12cb787227db5

	# path('users/<int:user_id>', views.profile, name='profile'),

	# Profile Page (Show)
	path('users/', views.profile, name='profile'),

	# path('users/<int:user_id>/edit', views.edit_profile, name='edit_profile'),

	# Edit
	path('users/edit/', views.edit_profile, name='edit_profile'),
<<<<<<< HEAD
	# Post Routes
=======

	# Post Routes--
>>>>>>> 39c0e53ac810d87fc9d749080fe12cb787227db5

	# Show
	path('posts/<int:post_id>', views.post, name='post'),
	# New
	path('posts/new', views.new_post, name='new_post'),

	# Delete
	path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
	
	# City Routes---
	path('cities/', views.cities, name='cities'),
	path('cities/london', views.london, name='london'),
	path('cities/sanfran', views.sanfran, name='sanfran'),
	path('cities/seattle', views.seattle, name='seattle'),
	path('cities/sydney', views.sydney, name='sydney'),


]