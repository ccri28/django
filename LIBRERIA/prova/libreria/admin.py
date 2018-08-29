from django.contrib import admin
from .models import Autore, Genere, Libro

# Register your models here.

admin.site.register(Autore)
admin.site.register(Libro)
admin.site.register(Genere)
