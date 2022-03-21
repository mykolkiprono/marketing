from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    available_stock = models.IntegerField()
    delivery = models.BooleanField()
    delivery_radius = models.CharField(max_length=20)
    desc = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    price = models.IntegerField()
