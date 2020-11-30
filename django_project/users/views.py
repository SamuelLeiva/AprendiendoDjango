from django.shortcuts import render, redirect
#clases para hacer forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #clase para usar flash messages
from .forms import UserRegisterForm #importamos nuestra form presonalizada

# Create your views here.
#Register view
def register(request):
    if request.method == 'POST': #si recibimos una post request, instancia una form con la data que pasamos como parametro
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #guarda nuestro usuario en nuestra BD
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}') #uso de flashed messages
            return redirect('blog-home') #name que le dimos en urls.py
    else:
        form = UserRegisterForm() #instancia una form vacia
    return render(request, 'users/register.html', {'form': form}) #pasamos la form como parametro a nuestra template

