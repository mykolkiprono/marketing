from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    @property
    def get_name():
        return self.User.first_name+" "+self.User.second_name

    def call():
        return first_name+" "+second_name
