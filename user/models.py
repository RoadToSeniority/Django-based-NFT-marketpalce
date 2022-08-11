from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    # A naSHi application
    username = models.IntegerField(unique=True, max_length=100)
    department = models.CharField(max_length=100)