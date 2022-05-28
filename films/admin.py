from django.contrib import admin

# Register your models here.
from .models import Film, Session, SessionsOfFilm

admin.site.register(Film)
admin.site.register(Session)
admin.site.register(SessionsOfFilm)
