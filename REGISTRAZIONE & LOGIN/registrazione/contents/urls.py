from django.urls import path
from .views import contenuti

urlpatterns = [
    path('contenuti/', contenuti, name='contenuti')
]
