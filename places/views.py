from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import *
from .models import *


class HellListView(generics.ListAPIView):
    serializer_class = HellListSerializer
    queryset = Hell.objects.all()


class HellDetailView(generics.RetrieveAPIView):
    serializer_class = HellDetailSerializer
    queryset = Hell.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('num', None)
        obj = get_object_or_404(queryset, num_hell=filter)
        return obj
