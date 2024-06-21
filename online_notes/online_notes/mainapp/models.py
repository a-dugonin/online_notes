from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Note(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
