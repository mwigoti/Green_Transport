from django.db import models
from email.policy import default

# Create your models here.

class Car(models.Model):
    car_id=models.IntegerField(default=0)
    car_name=models.CharField(max_length=30,default="")
    car_desc=models.CharField(max_length=300)