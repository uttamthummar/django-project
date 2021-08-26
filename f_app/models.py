from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class user(models.Model):
    name= models.CharField(max_length=100,null=True)
    phone=models.IntegerField(null=True)
    email=models.CharField(max_length=100,null=True)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)

class Clothes(models.Model):
    name=models.CharField(max_length=100,null=True)
    img = models.ImageField(upload_to="pics")
    price=models.IntegerField(null=True)