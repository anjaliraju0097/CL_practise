from django.db import models
from django. contrib. auth. base_user import AbstractBaseUser

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    age = models.IntegerField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.username

# class student(AbstractBaseUser):
    # username = models.CharField(max_length=200,blank=False)
    # gender = models.CharField(max_length = 10)
    # age = models.IntegerField()
    # email = models.EmailField(max_length = 200,blank=False)
    # password = models.CharField(max_length=100,blank=False)


