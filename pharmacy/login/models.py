from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user_login(AbstractUser):
    gender = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(default='', max_length=100)
    profetion = models.CharField(default="", max_length=100)
    filed = models.CharField(max_length=100, default='')
    def __str__(self):
            return (self.first_name + " " + self.last_name)
