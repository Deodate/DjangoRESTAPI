from django.db import models

# Create your models here.
class kigali(models.model):
    city_name = models.CharField(max_length=100)
    city_location = models.CharField(max_length=3)
    city_population = models.IntegerField()
