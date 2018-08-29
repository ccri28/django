from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')

def logoutForbidden(request):
    return render(request, 'core/forbidden_logout.html')

def contentsForbidden(request):
    return render(request, 'core/forbidden_content.html')

def profiloUtente(request, username):
    user = get_object_or_404(User, username=username)
    context = {"user":user}
    return render(request, 'core/profilo_utente.html', context)
