from django.db import models
from django.urls import reverse
# Create your models here.

class Genere(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"


class Autore(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse('dettaglio_autore', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"


class Libro(models.Model):
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"
