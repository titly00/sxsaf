from django.db import models


# Create your models here.

class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    brands_car = models.CharField(max_length=101)
    info = models.TextField()