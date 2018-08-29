from django.urls import path
from .views import homepage, logoutForbidden, contentsForbidden, profiloUtente

urlpatterns = [
    path('', homepage, name='homepage'),
    path('/out', logoutForbidden, name='out'),
    path('/con', contentsForbidden, name='con'),
    path('/profilo_utente/<username>', profiloUtente, name='profilo_utente')
]
