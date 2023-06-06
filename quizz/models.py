from django.db import models
from django.contrib.auth.models import User
class Partie(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) 
  points = models.IntegerField(default=0) 
  numquestion = models.IntegerField(default=1)