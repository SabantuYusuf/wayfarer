from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	# User Routes
	path('accounts/signup/', views.signup, name='signup'),
	path('users/<int:user_id>', views.profile, name='profile'),
	# City Routes
	path('cities/', views.cities, name='cities'),
]