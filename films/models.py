from django.db import models, transaction


class Film(models.Model):
    name_film = models.CharField('Название фильма', max_length=200)
    dic_film = models.TextField('Описание фильма')
    session_num = models.IntegerField('Количество сессий')

    def __str__(self):
        return self.name_film

    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs)
        for num in range(1, self.session_num + 1):
            session = Session.objects.create(film=self, num_session=num)
            SessionsOfFilm.objects.create(film=self, num_session=session)


class Session(models.Model):
    film = models.ForeignKey(Film, related_name='sessions', on_delete=models.CASCADE)
    num_session = models.IntegerField('Номер сессии')

    def __str__(self):
        return str(self.num_session)


class SessionsOfFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    num_session = models.ForeignKey(Session, on_delete=models.CASCADE)
