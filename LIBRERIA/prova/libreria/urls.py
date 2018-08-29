
from django.urls import path
from .views import ListaLibri, DettagliAutore

urlpatterns = [
    path('lista_libri/', ListaLibri.as_view(), name='lista_libri'),
    path('dettaglio_autore/<int:pk>', DettagliAutore.as_view(), name='dettaglio_autore')
]
