from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, Director, Category, Film
from .forms import AddFilmForm, AddDirectorForm
from django.views.generic import View, ListView, CreateView, DeleteView, DetailView, UpdateView
# Create your views here.


def home(request):
	film = Film.objects.all()
	director = Director.objects.all()
	return render(request, 'homepage.html', {'film':film, 'director':director})


class FilmListView(ListView):
	model = Film
	template_name = 'film_list.html'

class DirectorListView(ListView):
	model = Director
	template_name = 'director_list.html'


class AddFilm(CreateView):
	form_class = AddFilmForm
	template_name = 'addFilm.html'
	success_url = reverse_lazy('home')

class AddDirector(CreateView):
	form_class =  AddDirectorForm
	template_name = 'addDirector.html'
	success_url = reverse_lazy('home')



