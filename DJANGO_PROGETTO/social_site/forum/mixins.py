# mixin sono dei pezzi di codice che possiamo aggiungere alle nostre view
# che servono per effettuare una serie di controlli
from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):

    """ lo scopo di questo mixin è far creare nuove sezioni solo allo staff """

    def test_func(self):
        # il test passa soltanto se lo user è Staff
        return self.request.user.is_staff
        # qualora test_func restituisca True vuol dire che è tutto a posto
        # altrimenti il test non è superato
