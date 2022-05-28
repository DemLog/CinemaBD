from django.db import models
from films.models import Session
from places.models import Place


class Client(models.Model):
    phone = models.CharField('Номер телефона', max_length=10)
    name_client = models.CharField('Имя клиента', max_length=200)
    is_regular = models.BooleanField('Постояный ли клиент')
    num_buys = models.IntegerField('Количество покупок', default=0)

    def __str__(self):
        return "Клиент: {0} | Номер телефона: {1}".format(self.name_client, self.phone)


class Cashier(models.Model):
    name_cashier = models.CharField('Имя кассира', max_length=200)
    is_regular = models.BooleanField('Постояный ли клиент')  # ЗАЧЕМ?!?!?!?
    num_sales = models.IntegerField('Количество продаж', default=0)

    def __str__(self):
        return self.name_cashier


class Ticket(models.Model):
    num_ticket = models.AutoField('Номер билета', primary_key=True)
    num_session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.num_ticket)


class PurchaseTicket(models.Model):
    phone_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name_cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    num_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return "Клиент: {0} | Кассир: {1} | Номер билета: {2} | {3}".format(self.phone_client.name_client,
                                                                            self.name_cashier, self.num_ticket,
                                                                            self.place)
