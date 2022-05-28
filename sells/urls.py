from django.urls import path

from .views import *

app_name = 'sells'
urlpatterns = [
    path('getListClients', ClientListView.as_view()),
    path('getClient', ClientDetailView.as_view()),
    path('getListCashiers', CashierListView.as_view()),
    path('getCashier', CashierDetailView.as_view()),
    path('getListTickets', TicketListView.as_view()),
    path('getTicket', TicketDetailView.as_view()),
    path('getListPurchases', PurchaseTicketListView.as_view()),
    path('getPurchase', PurchaseTicketDetailView.as_view()),
    path('createPurchase', PurchaseTicketCreateView.as_view()),
]
