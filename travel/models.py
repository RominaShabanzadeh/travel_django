from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class travel_mdl(models.Model):
    name=models.CharField(max_length=30)
    origin=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    price=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")