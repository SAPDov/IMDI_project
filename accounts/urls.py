from django.urls import path, include
from . import views

urlpatterns = [
	path('signup', views.UserCreateView.as_view(), name= 'register'),
	path('login/', views.UserLoginView.as_view(), name='login'),
	path('logout/', views.UserLoginView.as_view(), name='login'),

	] 
