from django.urls import path

from .views import *

app_name = 'films'
urlpatterns = [
    path('getListFilms', FilmListView.as_view()),
    path('getFilm', FilmDetailView.as_view()),
]
