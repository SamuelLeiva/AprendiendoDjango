from django.shortcuts import render
#from django.http import HttpResponse #reemplazamos con render si usamos templates
from .models import Post #importando nuestros posts de la BD

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #leyendo el contenido de Post
    }
    return render(request, 'blog/home.html', context) #busca dentro de la carpeta templates
    #pasamos context como dato
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #los parametros 

