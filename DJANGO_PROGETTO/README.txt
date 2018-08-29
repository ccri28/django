-Per ogni progetto viene creato un nuovo v_env contenente i packages neccessari al progetto e le varie 
 dipendenze

1.Creo progetto 
2.Inizializzo il db
3.Crea account superuser
4.Creo app accounts
5.Creo form 
6.Creo View
7.vado a mappare la View
8.vado ad includere nel url django.contrib.urls per poter utilizzare le funzionalita' di login, logout,
password change, password reset, offerte dall'app auth
9.andiamo a creare una cartella registration, dentro template, che servira alla nostra app auth
10.creiamo i vari templates dentro registration
11.andiamo in settings e definiamo LOGIN_REDIRECT_URL = "/"

12.creo app core e forum
13.installo le apps in settings.py
14.vado a registrare il percorso dei templates
15.scrivo una nuova views dentro core, per la homepage
16.andiamo a creare il template corrispondente alla view
17.andiamo a mappare la views

18.Andiamo a creare dei modelli nel models.py, all'interno dell'app forum
19.makemigrations e migrate, pero' prima dobbiamo installare Pillow per il campo ImageField
   Pillow ci permette di utilizzare le immagini
20.Andiamo a registrare i modelli in admin.py
21.Andiamo ad aggiungere MEDIA_ROOT e MEDIA_URL in settings.py per le immagini che verranno caricate nelle sezioni
22.La cartella media root(media-serve) deve stare al di fuori del progetto
23.Andiamo in urls del progetto e andiamo a specificare static per gestire i media
"""
ALLA FINE, PER GESTIRE IL CARICAMENTO DELLE IMAGGINI NELLE NOSTRE SEZIONI, BASTA ANDARE IN SETTINGS.PY AD AGGIUNGERE 
"MEDIA_URL"(INDIRIZZO DAL QUALE I FILE VERRANNO SERVITI) & "MEDIA_ROOT"(CARTELLA DALLA QUALE I FILE VERRANNO SERVITI)
INOLTRE, AGGIUNGERE IN SETTINGS.PY ANCHE QUESTO 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
*i  file statici sono i file css, javascript e le immagini
"""

24.Andiamo a personalizzare admin.py aggiungendo dei ModelAdmin
25.Andiamo a specificare il percorso dei file statici dentro settings.py
26.Andiamo a creare una cartella "static-storage" contenente i file statici 

