from django.urls import path

from .views import *

app_name = 'places'
urlpatterns = [
    path('getListHells', HellListView.as_view()),
    path('getHell', HellDetailView.as_view()),
]
