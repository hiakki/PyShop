from django.db import models

# Create your models here.
class Product(models.Model):        # Model class defines common characteristics of our django app and will save it to DB
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) # Standard Maximum lengths for URLs


# Create a class for discount of 20%
class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=255)
    discount = models.FloatField()