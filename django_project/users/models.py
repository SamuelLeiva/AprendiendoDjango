from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Profile(models.Model):
    #a cada user le corresponde uno y solo un profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) #si eliminamos un usuario se eliminan los profiles
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self): #si mandamos a imprimir este model que se muestre lo siguiente
        return f'{self.user.username} Profile'