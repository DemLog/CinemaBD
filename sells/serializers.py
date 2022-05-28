from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from films.serializers import SessionDetailSerializer
from places.serializers import PlaceDetailSerializer
from .models import *


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone', 'name_client', 'is_regular', 'num_buys')


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('phone', 'name_client')


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


class PurchaseTicketCreateSerializer(serializers.ModelSerializer):
    client = ClientCreateSerializer()
    cashier = serializers.IntegerField()
    ticket = TicketDetailSerializer()
    place = serializers.IntegerField()

    class Meta:
        model = PurchaseTicket
        fields = ('client', 'cashier', 'ticket', 'place')

    # def create(self, validated_data):
    #     client = validated_data.pop('client', None)
    #     cashier = validated_data.pop('cashier', None)
    #     ticket = validated_data.pop('ticket', None)
    #     place = validated_data.pop('place', None)
    #
    #     if client:
    #         try:
    #             client = Client.objects.get(phone=client.phone)
    #         except ObjectDoesNotExist:
    #             client = Client(phone=client.phone, name_client=client.name_client)
    #             client.save()
    #     if cashier:
    #         try:
    #             cashier = Cashier.objects.get(id=cashier)
    #         except ObjectDoesNotExist:
    #             pass
    #     if place:
    #         try:
    #             place = Place.objects.get(id=place)
    #         except ObjectDoesNotExist:
    #             pass
    #
    #     Ticket.objects.create(ticket)
    #     client.num_buys += 1
    # НЕТ ВРЕМЕНИ




