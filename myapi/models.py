from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserRegister(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = None
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    def __str__(self):
        return self.name