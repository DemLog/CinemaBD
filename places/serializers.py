from rest_framework import serializers
from .models import *


class PlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('num_place', 'is_busy')


class HellDetailSerializer(serializers.ModelSerializer):
    places = PlaceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Hell
        fields = ('id', 'num_hell', 'num_places', 'places')


class HellListSerializer(serializers.ModelSerializer):
    num_free_places = serializers.IntegerField(source='get_num_free_places')
    num_occup_places = serializers.IntegerField(source='get_num_occup_places')

    class Meta:
        model = Hell
        fields = ('id', 'num_hell', 'num_places', 'num_free_places', 'num_occup_places')
