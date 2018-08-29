from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.decorators import login_required #decoratore
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import Sezione, Post, Discussione
from .mixins import StaffMixing
from .forms import DiscussioneModelForm, PostModelForm
from django.core.paginator import Paginator #EmptyPage, PageNotAnInteger

# Create your views here.

class CreaSezione(StaffMixing, CreateView):
    # la view crea un oggetto a partire da questo modello
    model = Sezione
    fields = "__all__"
    # CreateView ci offre gia' dei template di default,
    # ma è sempre bene essere specifici!
    template_name = "forum/crea_sezione.html"
    success_url = "/"


""" View che serve ad ottenere i dettagli di una singola sezione """
def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    # visualizziamo anche le discussioni di questa sezione
    discussioni_sezione = Discussione.objects.filter(sezione_appartenenza = sezione).order_by("-data_creazione")
    context = {"sezione":sezione, "discussioni": discussioni_sezione}
    return render(request, 'forum/singola_sezione.html', context)


# decoratore
# con questo decoratore andiamo a specificare che solo gli utenti loggati potranno creare nuove discussioni
@login_required
def creaDiscussione(request, pk):
    # sezione di appartenenza per la nostra discussione
    sezione = get_object_or_404(Sezione, pk=pk)
    if request.method == "POST":
        form = DiscussioneModelForm(request.POST)
        if form.is_valid():
            # andando ad utilizzare ModelForm posso utilizzare save()
            # con commit=False posso andare a sospendere per un po' la creazione dell'oggetto, andando ad aggiungere degli attributi aggiuntivi
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore_discussione = request.user
            discussione.save()
            # contenuto passato tramite il nostro form
            primo_post = Post.objects.create(discussione=discussione, autore_post = request.user,
                                             contenuto = form.cleaned_data["contenuto"])
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        form = DiscussioneModelForm()
    context = {"form":form, "sezione":sezione}
    return render(request, 'forum/crea_discussione.html', context)


# view che ci permette di visualizzare i dettagli di una singola discussione
# oltre alla discussione vogliamo anche i posts, ad essa associati
def visualizzaDiscussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    # con filter possiamo andare a selezionare una queryset a partire dai dettagli che andiamo a specificare
    # quindi una sotto query, sotto lista di risultati in base alle specifiche che passiamo a filter
    posts_discussione = Post.objects.filter(discussione = discussione)

    # andiamo a specificare quanti post vogliamo visualizzare per pagina
    paginator = Paginator(posts_discussione, 5)
    # vado a prendere il valore dal dizionario di GET
    # pagina indica la pagina corrente
    page = request.GET.get("pagina")
    # richiamo il metodo get_page sull'oggetto Paginator
    # page indica la pagina corrispondente in cui ci troviamo
    # posts rappresenta un sotto query set che rappresenta gli elementi per la pagina che stiamo visualizzando
    posts = paginator.get_page(page)

    form_risposta = PostModelForm()
    context = {"discussione":discussione,
               "posts_discussione":posts,
               "form_risposta":form_risposta}
    return render(request, 'forum/singola_discussione.html', context)


@login_required
# pk indica la chiave primaria della discussione, per la quale andiamo ad aggiungere il post
def aggiungiRisposta(request, pk):
    # discussione di appartenenza del nostro post
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        # poi andiamo a prendere questo form, e lo aggiungiamo al context di visualizzaDiscussione
        # lo identifichiamo con form_risposta
        form = PostModelForm(request.POST)
        if form.is_valid():
            # commit = False, in quanto dobbiamo ancora aggiungere dei dati
            form.save(commit=False)
            form.instance.discussione = discussione
            form.instance.autore_post = request.user
            form.save()
            # in questo caso la pk è quella passata tramite url
            url_discussione = reverse("visualizza_discussione", kwargs={"pk":pk})
            pagine_in_discussione = discussione.get_n_pages()
            # se è presente piu' di una pagina
            if pagine_in_discussione > 1:
                success_url = url_discussione + "?pagina=" + str(pagine_in_discussione)
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponseRedirect(url_discussione)

    else:
        return HttpResponseBadRequest()
            # passeremmo il form alla funzione visualizzaDiscussione
            # e accettiamo una risposta di tipo Post
            # quindi diversamente, il metodo della richiesta non sia post,
            # allora andiamo a richiamare una funzione che si chiama response bad request


""" andiamo a creare una class based view utilizzata per creare una funzione che ci permette di cancellare i post """
class CancellaPost(DeleteView):
    model = Post
    # url di indirizzamento
    success_url = "/"
    # abbiamo bisogno di un template per chiedere la conferma della cancellazione di un post
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autore_post_id = self.request.user.id )
