from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import *
from .models import *


class ClientListView(generics.ListAPIView):
    serializer_class = ClientDetailSerializer
    queryset = Client.objects.all()


class ClientDetailView(generics.RetrieveAPIView):
    serializer_class = ClientDetailSerializer
    queryset = Client.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        return obj


class CashierListView(generics.ListAPIView):
    serializer_class = CashierDetailSerializer
    queryset = Cashier.objects.all()


class CashierDetailView(generics.RetrieveAPIView):
    serializer_class = CashierDetailSerializer
    queryset = Cashier.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        return obj


class TicketListView(generics.ListAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()


class TicketDetailView(generics.RetrieveAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('num', None)
        obj = get_object_or_404(queryset, num_ticket=filter)
        return obj


class PurchaseTicketListView(generics.ListAPIView):
    serializer_class = PurchaseTicketDetailSerializer
    queryset = PurchaseTicket.objects.all()


class PurchaseTicketDetailView(generics.RetrieveAPIView):
    serializer_class = PurchaseTicketDetailSerializer
    queryset = PurchaseTicket.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        return obj
