from django.db import models

# Create your models here.
class unitconv(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=100)
    conversionFactor = models.FloatField()
