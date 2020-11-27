from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #ruta: /
    path('about/', views.about, name='blog-about')
] #urls de nuestra pagina