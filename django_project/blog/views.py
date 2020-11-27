from django.shortcuts import render
#from django.http import HttpResponse #reemplazamos con render si usamos templates

#dummy data
posts = [
    {
        'author': 'SamuelLeiva',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2013'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2013'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts #data que se va a mandar a nuestros templates
    }
    return render(request, 'blog/home.html', context) #busca dentro de la carpeta templates
    #pasamos context como dato
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #los parametros 

