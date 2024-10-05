from django.db import models
from django.utils import timezone


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    updated = models.DateField(auto_now_add=True)