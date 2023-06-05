from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Shopper(AbstractUser):
     username = models.CharField(max_length=30, unique=True) 
     email = models.EmailField()
     password = models.CharField(max_length=15)
     phone_number = models.CharField(max_length=20)

     def __str__(self):

        return self.username
 




