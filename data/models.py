from django.db import models
from django.conf import settings


class EnergyPrice(models.Model):

    date = models.DateField()
    SE1 = models.CharField(max_length=255)
    SE2 = models.CharField(max_length=255)
    SE3 = models.CharField(max_length=255)
    SE4 = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date)
