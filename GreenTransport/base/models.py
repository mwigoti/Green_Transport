from django.db import models
from email.policy import default

# Create your models here.

class Car(models.Model):
    car_id=models.IntegerField(default=0)
    car_name=models.CharField(max_length=30,default="")
    car_desc=models.CharField(max_length=300, default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="car/images", default="")

    def __str__(self):
        return self.car_name
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=90, default="")

    
