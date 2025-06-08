from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    email=models.EmailField(unique=True,null=True,blank=True)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)
    salary=models.CharField(max_length=25,null=True,blank=True,default=10000)
    
    def __str__(self):
        return self.name