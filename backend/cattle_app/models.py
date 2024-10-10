from django.db import models


class Cattle(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    birth = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return self.name
