from django.urls import path
from .views import contenutiView

urlpatterns = [

    path('contenuti/', contenutiView, name='contenuti'),

]
