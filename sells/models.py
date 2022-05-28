from django.db import models
from films.models import Session

class Client(models.Model):
	phone = models.CharField('Номер телефона', max_length = 10)
	name_client = models.CharField('Имя клиента', max_length = 200)
	is_regular = models.BooleanField('Постояный ли клиент')
	num_buys = models.IntegerField('Количество покупок')

	def __str__(self):
		return self.phone

class Cashier(models.Model):
	name_cashier = models.CharField('Имя кассира', max_length = 200)
	is_regular = models.BooleanField('Постояный ли клиент')
	num_sales = models.IntegerField('Количество продаж')

	def __str__(self):
		return self.name_cashier

class Ticket(models.Model):
	num_ticket = models.IntegerField('Номер билета')
	num_session=models.ForeignKey(Session, on_delete = models.CASCADE)

	def __str__(self):
		return self.num_ticket

class PurchaseTicket(models.Model):
	phone_client = models.ForeignKey(Client, on_delete = models.CASCADE)
	name_cashier = models.ForeignKey(Cashier, on_delete = models.CASCADE)
	num_ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE)
	place = models.IntegerField('Номер места')