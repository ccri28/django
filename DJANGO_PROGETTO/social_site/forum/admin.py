from django.contrib import admin
from .models import Sezione, Discussione, Post

class DiscussioneModelAdmin(admin.ModelAdmin):
    model = Discussione
    #specifichiamo delle liste col contenuto che vogliamo personalizzare
    #questi campi verranno visualizzati nella sezione amministrazione
    list_display = ["titolo", "sezione_appartenenza", "autore_discussione"]
    #specifichiamo un'altra lista coi campi ricercabili
    #campi che potranno essere ricercati dal campo search, presente nel
    #pannello di controllo
    search_fields = ["titolo", "autore_discussione"]
    #specifichiamo una lista di campi filtrabili
    list_filter = ["sezione_appartenenza", "data_creazione"]


class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["discussione", "autore_post"]
    search_fields = ["contenuto"]
    list_filter = ["data_creazione", "autore_post"]


class SezioneModelAdmin(admin.ModelAdmin):
    model = Sezione
    list_display = ["nome_sezione", "descrizione"]



# Register your models here.
admin.site.register(Sezione, SezioneModelAdmin)
admin.site.register(Discussione, DiscussioneModelAdmin)
admin.site.register(Post, PostModelAdmin)
