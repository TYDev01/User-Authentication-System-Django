from django import forms

from .models import NewUser
from django.contrib.auth.forms import UserCreationForm

class CustomUser(UserCreationForm):
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    phoneNumber = forms.IntegerField(max_value=15, required=True)

    class Meta:
        model = NewUser
        fields = [ 'firstname', 'lastname', 'username', 'email', 'password1', 'password2', 'phoneNumber']