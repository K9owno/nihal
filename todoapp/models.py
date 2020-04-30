from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(User,default=None, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.author

class login(models.Model):
    Username = models.CharField(max_length=100)

