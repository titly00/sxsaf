from django.db import models


# Create your models here.

class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    brands_car = models.CharField(max_length=101)
    info = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=123)





class Book(models.Model):
    titel = models.CharField(max_length=103)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)


class Car(models.Model):
    name = models.CharField(max_length=122)
    Author = models.CharField(max_length=123)
    info = models.TextField()




