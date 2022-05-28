from django.contrib import admin

from .models import Client, Cashier, Ticket, PurchaseTicket

admin.site.register(Client)
admin.site.register(Cashier)
admin.site.register(Ticket)
admin.site.register(PurchaseTicket)
