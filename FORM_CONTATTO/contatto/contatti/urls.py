from django.urls import path
from .views import MessaggioView

urlpatterns = [
    path('scrivici/', MessaggioView, name='scrivici')
]
