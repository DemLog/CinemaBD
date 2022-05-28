from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import *
from .models import *


class FilmListView(generics.ListAPIView):
    serializer_class = FilmListSerializer
    queryset = Film.objects.all()


class FilmDetailView(generics.RetrieveAPIView):
    serializer_class = FilmDetailSerializer
    queryset = Film.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        return obj
