from django.db import models


class Hell(models.Model):
    num_hell = models.IntegerField('Номер зала')
    num_places = models.IntegerField('Количество Мест')

    # num_free_places = models.IntegerField('Количество Свободных Мест')
    # num_occup_places = models.IntegerField('Количество Занятых Мест')

    def __str__(self):
        return "Зал {0}".format(self.num_hell)

    def save(self, *args, **kwargs):
        super(Hell, self).save(*args, **kwargs)
        for place in range(1, self.num_places + 1):
            Place.objects.create(num_place=place, num_hell=self)

    def get_num_free_places(self):
        places = Place.objects.filter(num_hell=self)
        free_places = 0
        for place in places:
            if not place.is_busy:
                free_places += 1
        return free_places

    def get_num_occup_places(self):
        places = Place.objects.filter(num_hell=self)
        occup_places = 0
        for place in places:
            if place.is_busy:
                occup_places += 1
        return occup_places


class Place(models.Model):
    is_busy = models.BooleanField('Занято ли место?', default=False)
    num_place = models.IntegerField('Номер Места')
    num_hell = models.ForeignKey(Hell, related_name='places', on_delete=models.CASCADE)

    def __str__(self):
        return "Зал: {0} | Место: {1}".format(self.num_hell.num_hell, self.num_place)
