from rest_framework import serializers

from films.serializers import SessionDetailSerializer
from places.serializers import PlaceDetailSerializer
from .models import *


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone', 'name_client', 'is_regular', 'num_buys')


class CashierDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashier
        fields = ('id', 'name_cashier', 'is_regular', 'num_sales')


class TicketDetailSerializer(serializers.ModelSerializer):
    num_session = SessionDetailSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ('num_ticket', 'num_session')


class PurchaseTicketDetailSerializer(serializers.ModelSerializer):
    phone_client = ClientDetailSerializer(read_only=True)
    name_cashier = CashierDetailSerializer(read_only=True)
    num_ticket = TicketDetailSerializer(read_only=True)
    place = PlaceDetailSerializer(read_only=True)

    class Meta:
        model = PurchaseTicket
        fields = ('id', 'phone_client', 'name_cashier', 'num_ticket', 'place')
