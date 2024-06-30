from django.db import models

# Create your models here.
class Item(models.Model):
    cityName = models.CharField(max_length=100)
    countryName = models.CharField(max_length=100)
    year = models.IntegerField()
    population = models.IntegerField()

    def __str__(self):
        return self.cityName

