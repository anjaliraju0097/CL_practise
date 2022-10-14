from enum import unique
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserRegister(AbstractUser):

    # SUCCESS = 'S'
    # FAILED = 'F'
    # REG_STATUS = ((SUCCESS, 'Success'),
    #                        (FAILED, 'Failed'))
    id = models.AutoField(primary_key=True)
    username = None
    #status = models.CharField(max_length=1, default=SUCCESS, choices=REG_STATUS, null=True, blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    def __str__(self):
        return self.name


