from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    ) #importamos listview para listar los posts
#from django.http import HttpResponse #reemplazamos con render si usamos templates
from .models import Post #importando nuestros posts de la BD

# Create your views here.
#function-based view
def home(request):
    context = {
        'posts': Post.objects.all() #leyendo el contenido de Post
    }
    return render(request, 'blog/home.html', context) #busca dentro de la carpeta templates
    #pasamos context como dato

#class-based view -> puede usar menos codigo
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #buscara home.html en ves de post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordena nuestros posts para mas recientes primero

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):#LRMixin hace que se redirija a la pagina de login si se quiere crear un post sin estar loggeados
    model = Post
    fields = ['title', 'content'] #tipos de fields pasados a la form
    #sobreescribimos este metodo
    def form_valid(self, form):
        form.instance.author = self.request.user #indicamos el usuario del post
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):#LRMixin hace que se redirija a la pagina de login si se quiere crear un post sin estar loggeados
    model = Post
    fields = ['title', 'content'] #tipos de fields pasados a la form
    #sobreescribimos este metodo
    def form_valid(self, form):
        form.instance.author = self.request.user #indicamos el usuario del post
        return super().form_valid(form)

    def test_func(self): #verifica si el el usuario es autor del post a actualizar
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #lo enviamos a home si es eliminado exitosamente
    def test_func(self): #verifica si el el usuario es autor del post a actualizar
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #los parametros 

