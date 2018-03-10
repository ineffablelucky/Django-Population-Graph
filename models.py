from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Graph(models.Model):

    year = models.PositiveIntegerField(validators=[MaxValueValidator(9999),], unique=True)
    population = models.PositiveIntegerField()
    growth = models.PositiveIntegerField()
    growth_rate = models.FloatField()

    def __str__(self):
        return  '%s' % (self.year)
