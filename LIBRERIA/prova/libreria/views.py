from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Autore, Libro

# Create your views here.

#Class Based Views
class ListaLibri(ListView):
    model = Libro
    template_name = 'libreria/lista_libri.html'
    context_object_name = 'lista_libri'

class DettagliAutore(DetailView):
    model = Autore
    template_name = 'libreria/dettaglio_autore.html'
    
