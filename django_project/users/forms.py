from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #agregamos el campo de Email

    class Meta:
        model = User #indica que va a crear un nuevo usuario
        fields = ['username',  'email', 'password1', 'password2']

