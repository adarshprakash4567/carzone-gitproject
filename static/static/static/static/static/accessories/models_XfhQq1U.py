from django.db import models
#from datetime import datetime
# Create your models here.
class Accessories(models.Model):


    car_title=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    conditions = models.CharField(max_length=100)
    price = models.IntegerField()