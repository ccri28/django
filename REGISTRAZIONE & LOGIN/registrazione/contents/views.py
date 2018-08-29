from django.shortcuts import render

# Create your views here.

def contenuti(request):
    return render(request, 'contents/contenuti.html')
