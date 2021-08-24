from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import ProfileForm


# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			profile = profile_form.save(commit=False)
			profile.user = new_user
			profile.user.save()
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
			if user:
				login(request, user)
				print('logged in')
			return redirect('home')
		else:
			form = UserCreationForm(request.POST)
	elif request.method == 'GET':
		form = UserCreationForm()
		profile_form = ProfileForm()
	return render(request, 'register.html', {'form': form, 'profile_form': profile_form})

