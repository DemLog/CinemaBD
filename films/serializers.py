from rest_framework import serializers
from .models import *


class SessionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'num_session')


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name_film', 'dic_film', 'session_num')


class FilmDetailSerializer(serializers.ModelSerializer):
    sessions = SessionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ('id', 'name_film', 'dic_film', 'sessions')


class SessionOfFilmDetailSerializer(serializers.ModelSerializer):
    film = FilmDetailSerializer(read_only=True)
    num_session = SessionDetailSerializer(read_only=True)

    class Meta:
        model = SessionsOfFilm
        fields = ('id', 'film', 'num_session')
