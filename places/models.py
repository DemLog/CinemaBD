from django.db import models


class Hell(models.Model):
    num_hell = models.IntegerField('Номер зала')
    num_places = models.IntegerField('Количество Мест')
    num_free_places = models.IntegerField('Количество Свободных Мест')
    num_occup_places = models.IntegerField('Количество Занятых Мест')

    def __str__(self):
        return self.num_hell


class Place(models.Model):
    is_busy = models.BooleanField('Занято ли место?')
    num_place = models.IntegerField('Номер Места')
    num_hell = models.ForeignKey(Hell, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_place
