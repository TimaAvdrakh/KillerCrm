from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField( unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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




