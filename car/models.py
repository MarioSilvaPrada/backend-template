from django.db import models
from user.models import User

class Car(models.Model):
    
    vendor = models.CharField(max_length=155)
    vehicle_id = models.UUIDField()
    user =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.vendor