from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_films', views.FilmListView.as_view(), name = 'all_films'),
    path('show_directors', views.DirectorListView.as_view(), name = 'all_directors'),
    path('add_film', views.AddFilm.as_view(), name = 'create_film'),
    path('add_director', views.AddDirector.as_view(), name = 'create_director'),
]
