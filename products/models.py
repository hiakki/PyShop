from django.db import models

# Create your models here.
class Product(models.Model):        # Model class defines common characteristics of our django app and will save it to DB
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) # Standard Maximum lengths for URLs