from django.urls import path
from .views import homepage, profilo_utente

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profilo_utente/', profilo_utente, name='profilo_utente')
]
