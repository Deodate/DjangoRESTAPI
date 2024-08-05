from django.db import models

# Create your models here.
class Kigali(models.Model):
    city_name = models.CharField(max_length=100)
    city_location = models.CharField(max_length=3)
    city_population = models.IntegerField()

    def __str__(self):
        return self.city_name
