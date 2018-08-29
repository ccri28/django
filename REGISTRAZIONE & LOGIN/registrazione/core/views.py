from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')

def profilo_utente(request):
    return render(request, 'core/profilo_utente.html')
