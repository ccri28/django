from django.shortcuts import render, HttpResponseRedirect
from .forms import FormRegistrazione
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def registrazioneView(request):
    if request.method == 'POST':
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()
    context={"form":form}
    return render(request, 'accounts/registrazione.html', context)
