from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .forms import UserSignupForm, UserLoginForm
from django.urls import reverse_lazy

# Create your views here.

# def signup(request):
# 	if request.method == 'GET':
# 		form = UserSignupForm()
# 	elif request.method == 'POST':
# 		form = UserSignupForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			return redirect('home')
# 	else:
# 		return render(request, 'signup.html', {'form': form})


class UserCreateView(CreateView):
	form_class = UserSignupForm
	template_name = 'signup.html'
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		super().form_valid(form)
		user = authenticate(self.request, username=form.cleaned_data['username'],
		password=form.cleaned_data['password'])
		if user:
			login(self.request, user)
			return redirect('home')
		else:
			return self.form_invalid(form)



class UserLoginView(LoginView):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		return super().get(request, *args, **kwargs)

