from django.urls import path
from . import views

urlpatterns = [
    path('nuova-sezione/', views.CreaSezione.as_view(), name='crea_sezione'),
    path('sezione/<int:pk>/', views.visualizzaSezione, name='sezione_view'),
    path('sezione/<int:pk>/crea_discussione', views.creaDiscussione, name='crea_discussione'),
    path('discussione/<int:pk>/', views.visualizzaDiscussione, name='visualizza_discussione'),
    path('discussione/<int:pk>/rispondi/', views.aggiungiRisposta, name='rispondi_a_discussione'),
    # id e pk sono la stessa cosa, ma le usiamo per non confonderci
    # id indica l'id della discussione, e pk il pk del post che vogliamo cancellare
    path('discussione/<int:id>/cancella-post/<int:pk>', views.CancellaPost.as_view(), name='cancella_post')
]
