from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	# User Routes
	path('accounts/signup/', views.signup, name='signup'),
	path('users/<int:user_id>', views.profile, name='profile'),
	path('users/<int:user_id>/edit', views.edit_profile, name='edit_profile'),
	# City Routes
	path('cities/', views.cities, name='cities'),
	path('cities/london', views.london, name='london'),
]