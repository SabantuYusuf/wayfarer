from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	# User Routes
	path('accounts/signup/', views.signup, name='signup'),

	# path('users/<int:user_id>', views.profile, name='profile'),
	path('users/', views.profile, name='profile'),

	# path('users/<int:user_id>/edit', views.edit_profile, name='edit_profile'),
	path('users/edit/', views.edit_profile, name='edit_profile'),
	# Post Routes
	# Show
	path('posts/<int:post_id>', views.post, name='post'),
	path('posts/new', views.new_post, name='new_post'),
	# Add Post
  	# path('users/<int:user_id>/assoc_posts/<int:new_post_id>', views.assoc_posts, name='assoc_posts'),

	# City Routes
	path('cities/', views.cities, name='cities'),
	path('cities/london/', views.london, name='london'),
]