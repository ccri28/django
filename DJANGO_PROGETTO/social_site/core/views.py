from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from forum.models import Sezione, Discussione, Post


# Create your views here.

# def homepage(request):
#     return render(request, 'core/homepage.html')

class HomeView(ListView):

    """
    - queryset, nel nostro caso, rappresenta l'elenco delle sezioni presenti nel nostro sito
    - a differenza di ' model = ... ', queryset ci permette di applicare dei filtri e di
      ordinare il nostro queryset
    """
    queryset = Sezione.objects.all()
    template_name = 'core/homepage.html'
    """ grazie a questo, andiamo a rimpiazzare il nome object_list con il nome lista_sezioni """
    context_object_name = "lista_sezioni"


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/users.html'
    context_object_name = 'lista_utenti'



def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    # autore discussione = user del profilo
    # -pk indica l'ordine decrescente delle discussioni, in modo tale da vedere le ultime discussioni create per prime
    discussioni_utente = Discussione.objects.filter(autore_discussione=user).order_by("-pk")
    context = {"user":user, "discussioni_utente":discussioni_utente}
    return render(request, 'core/user_profile.html', context)

""" Vogliamo effettuare una ricerca per i post, user e discussioni """
def cerca(request):
    # se è presente il valore associato a q, all'interno di request.GET
    if "q" in request.GET:
        # allora andiamo a prendere il valore associato a q
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
            return redirect("/cerca/")
        # Con icontains possiamo vedere se i valori associati ai titoli contengono questa porzione di querystring (valori associati a questa querystring)
        discussioni = Discussione.objects.filter(titolo__icontains=querystring)
        posts = Post.objects.filter(contenuto__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {
            "discussioni":discussioni,
            "posts":posts,
            "users":users
        }
        return render(request, "core/cerca.html", context)
    else:
        return render(request, "core/cerca.html")
