from django.shortcuts import render

# Create your views here.

def contenutiView(request):
    return render(request, 'contents/contenuti.html')
