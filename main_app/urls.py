from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	# USER ROUTE
	# Sign Up
	path('accounts/signup/', views.signup, name='signup'),
	# Profile Page (Show)
	path('users/', views.profile, name='profile'),
	# NEEDS FUTURE WORK
	# path('users/(?P<id>[\w\-]+)/$', views.profiles, name='profiles'),
	# ^^ Credits: https://stackoverflow.com/questions/41125152/view-profile-page-as-another-user-in-django/41267943
	# Edit
	path('users/edit/', views.edit_profile, name='edit_profile'),
	# POST ROUTES
	# Show
	path('posts/<int:post_id>', views.post, name='post'),
	# New
	path('posts/new', views.new_post, name='new_post'),
	path('posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
	# Delete
	path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
	# City Routes---
	path('cities/', views.cities, name='cities'),
	path('cities/london', views.london, name='london'),
	path('cities/san-francisco', views.sanfran, name='sanfran'),
	path('cities/seattle', views.seattle, name='seattle'),
	path('cities/sydney', views.sydney, name='sydney'),
]