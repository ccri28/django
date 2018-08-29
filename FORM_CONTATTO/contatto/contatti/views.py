from django.shortcuts import render, HttpResponseRedirect
from .forms import MessaggioForm
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def MessaggioView(request):
    if request.method=="POST":
        form = MessaggioForm(request.POST)
        if form.is_valid():
            nuovo_messaggio = form.save()
            return HttpResponseRedirect("/")
    else:
        form = MessaggioForm()
    context = {"form":form}
    return render(request, 'contatti/form_contatto.html', context)
