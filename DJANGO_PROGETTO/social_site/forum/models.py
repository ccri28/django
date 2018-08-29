from django.db import models
# questo perche' sono gli utenti a creare le discussioni del nostro forum ecc...
# e perche' ogni utente viene rappresentato da questo modello
from django.contrib.auth.models import User
from django.urls import reverse
""" Ceil ci resituisce il numero intero successivo al float passato come parametro
    Per esempio, se il numero è 3.1 allora ceil ci restituisce 4self.
    Se il numero è intero, restituisce lo stesso numero intero. """
from math import ceil

# Create your models here.

class Sezione(models.Model):
    """
    le sezioni dividono il sito per categorie di discussione
    ciascuna sezione contiene svariate discussioni
    create dagli amministratori del sito

    Intanto non abbiamo bisogno di un campo utente o cretatore,
    in quanto saranno gli amministratori a creare le nuove sezioni
    """
    nome_sezione = models.CharField(max_length=80)
    #blank e null vanno a specificare che la descrizione non e' necessaria!
    #blank è a livello di validazione & null a livello di database
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse('sezione_view', kwargs={"pk":self.pk})

    # mostraci le ultime due discussioni
    def get_last_discussions(self):
        # [:2] indica una sotto lista, indica dalla prima alla seconda
        # infatti abbiamo bisogno delle utlime due discussioni
        return Discussione.objects.filter(sezione_appartenenza=self).order_by("-data_creazione")[:2]

    # andiamo a richiamare questo metodo, per un'istanza di tipo sezione
    # e per quest'istanza andiamo a vedere le discussioni,
    # quindi poi andiamo a prendere i post che sono presenti per quelle discussioni
    # con count otteniamo il numero dei post delle discussioni, che fanno parte di questa sezione
    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione_appartenenza=self).count()

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"


class Discussione(models.Model):
    titolo = models.CharField(max_length=120)
    #auto_now_add fa in modo che la data di creazione sia setata quando creiamo la discussione
    data_creazione = models.DateTimeField(auto_now_add=True)
    #usiamo User, perche sono gli user a creare le discussioni
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussioni")
    # *
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse('visualizza_discussione', kwargs={"pk":self.pk})

    """ indica il numero di pagine presenti nella discussione """
    def get_n_pages(self):
        # andiamo a prendere il numero di post
        # utilizziamo post_set perche' non abbiamo utilizzato il related name
        posts_discussione = self.post_set.count()
        n_pagine = ceil(posts_discussione/5)
        return n_pagine

    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural = "Discussioni"


class Post(models.Model):
    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
