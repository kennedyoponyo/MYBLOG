from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.username