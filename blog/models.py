from django.db import models

# Create your models here.
class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=100, unique=True)
   body = models.TextField()
   posted = models.DateField(db_index=True, auto_now_add=True)
   thumbnail = models.CharField(max_length=2083)
#   category = models.ForeignKey('blog.Category')

class Categorie(models.Model):
   title = models.CharField(max_length=100, db_index=True)
   slug = models.SlugField(max_length=100, db_index=True)