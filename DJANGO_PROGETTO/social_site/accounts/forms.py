from django import forms
# form gia' implementato presente nell'app auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    #oltre al username e password abbiamo bisogno
    #anche di una mail
    email = forms.CharField(max_length=20, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
