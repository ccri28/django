from django import forms
from .models import Messaggio

class MessaggioForm(forms.ModelForm):
    class Meta:
        model = Messaggio
        fields = "__all__"
        widgets = {
            "contenuto": forms.Textarea(attrs={"rows":5})
        }
