from typing import DefaultDict
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField

# Create your models here.
class CustomUser(AbstractUser):
    first_name=CharField(max_length=50)
    last_name=CharField(max_length=50)
    
    profile = models.ImageField( default='path/to/my/default/image.jpg')
    age = models.PositiveIntegerField(null=True, blank=True)
    is_patient = models.BooleanField(default='True')
    address = models.TextField(null=True, blank=True)