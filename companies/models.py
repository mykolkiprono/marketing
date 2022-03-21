from django.db import models
from products.models import product

# Create your models here.m

class company(models.Model):
    company_name = models.CharField(max_length=30)
    logo = models.ImageField(null=True,blank=True)
    c_image_1 = models.ImageField()
    c_image_2 = models.ImageField()
    c_image_3 = models.ImageField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
