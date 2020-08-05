from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	# User Routes
	# path('login/', views.login, name='login'),
	path('signup/', views.signup, name='signup'),
	# City Routes
	path('cities/', views.cities, name='cities'),
]