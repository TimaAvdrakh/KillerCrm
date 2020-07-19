from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

class Victim(models.Model):
    username = models.CharField(unique=True, max_length=20)
    age = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()
    link = models.CharField(max_length=20)
    dead = models.BooleanField(default=False)

    def __str__(self):
        self.username

class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    victims = models.ManyToManyField(Victim)




