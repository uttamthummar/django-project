from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class user(models.Model):
    name= models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)