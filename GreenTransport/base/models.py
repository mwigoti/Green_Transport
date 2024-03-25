from django.db import models
from email.policy import default

# Create your models here.

class Car(models.Model):
    car_id=models.IntegerField(default=0)
    