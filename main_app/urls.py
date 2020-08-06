from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	# User Routes
	path('accounts/signup/', views.signup, name='signup'),
	path('users/<int:user_id>', views.profile, name='profile'),
	
	# Posts
	path('posts/<int:post_id>', views.post, name='post_show'),
	path('posts/new', views.new_post, name='new_post'),
	
	# City Routes
	path('cities/', views.cities, name='cities'),
]