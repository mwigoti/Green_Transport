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
    email=models.EmailField()
    phone=models.CharField(max_length=13,default="")
    address=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    cars=models.ForeignKey(Car, on_delete=models.CASCADE)
    days_for_rent=models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    loc_from=models.CharField(max_length=50,default="")
    loc_to=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name
    




    
