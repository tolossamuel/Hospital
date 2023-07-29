from django.db import models
from stor.models import *
# Create your models here.
class pay(models.Model):
    patient = models.ForeignKey(Register_Patient, on_delete=models.CASCADE, default=None)
    price = models.IntegerField(default=0)
class ditale_price(models.Model):
    price = models.IntegerField(default=0)
    source = models.CharField(max_length=100)
    patient = models.ForeignKey(Register_Patient, on_delete=models.CASCADE, default=None)
    time_date = models.DateTimeField(auto_now=True)
class total_price(models.Model):
    total_price = models.IntegerField(default=0)