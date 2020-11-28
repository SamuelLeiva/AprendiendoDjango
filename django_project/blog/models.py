from django.db import models #ver en docs los tipos de field
from django.utils import timezone
from django.contrib.auth.models import User

#Modelos de Usuarios y posts

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #fecha actual
    author = models.ForeignKey(User, on_delete=models.CASCADE) #si el usuario es eliminado, se eliminaran sus posts

    def __str__(self):
        return self.title