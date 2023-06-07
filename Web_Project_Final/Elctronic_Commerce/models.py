from django.db import models
from django.contrib.auth.models import User

 
class device(models.Model):
    laptopType = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=350)
    briefDescription = models.CharField(max_length=100)

    
    def __str__(self) -> str:
        return f"{self.laptopType},{self.price},{self.description}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    devices = models.ManyToManyField(device)