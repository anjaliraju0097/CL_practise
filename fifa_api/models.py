from email.policy import default
from django.db import models

# Create your models here.
from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# class Event(models.Model):
#     Event_id = models.AutoField(primary_key=True)
#     Date = models.DateField()
#     Description = models.CharField(max_length=200)
#     Venue = models.CharField(max_length=100)



# class Fixture(models.Model):
#     Event_id = models.ForeignKey()
#     M_id = models.AutoField(primary_key=True)
#     Time = models.DateField()
#     Team_A = models.ForeignKey()
#     Team_B = models.ForeignKey()
#     Venue = models.CharField()
#     Result_id = models.ForeignKey()


class Teams(models.Model):

    team_id = models.AutoField(primary_key = True)
    group = models.CharField(max_length = 1) 
    name = models.CharField(max_length = 100,unique=True )
    coach = models.CharField(max_length = 100)
    status = models.BooleanField(default = '1', editable = False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    fav_team = models.ForeignKey(Teams, to_field='team_id',on_delete=models.PROTECT)
    points = models.CharField(max_length=100,null = True,blank=True)
    email = models.EmailField(max_length=100,unique=True,null=False,blank=False,default='')
    password = models.CharField(max_length=100,null=False,blank=False)
    

    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name








# class Questions(models.Model):
#     Q_id = models.IntegerField()
#     Questions = models.CharField(max_length=350)

# class Answers(models.Model):
#     Ans_id = models.AutoField(primary_key=True)
#     Q_id = models.ForeignKey()
#     U_id = models.ForeignKey()
#     Match_no = models.ForeignKey()
#     Answers = models.CharField(max_length=200)

# class Correct_Answers(models.Model):
#     Result_id = models.AutoField(primary_key=True)
#     Match_no = models.ForeignKey()
#     Q_id = models.ForeignKey()
#     Result = models.CharField(max_length=250)


# class Team(models.Model):
#     Group = models.CharField(max_length=100) 
#     Team_id = models.IntegerField()
#     Name = models.CharField(max_length=100)
#     Coach = models.CharField(max_length=100)

# class Players(models.Model):
#     Player_id = models.AutoField(primary_key=True)
#     P_name = models.CharField(max_length=100)
#     T_id = models.ForeignKey()
#     Position = models.CharField(max_length=100)
    
# class point_table(models.model):
#     point_id = models.AutoField(primary_key=True)
#     team_id = models.ForeignKey









