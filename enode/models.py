from django.db import models
from django.conf import settings


class EnodeTokenModel(models.Model):
    
    access_token = models.CharField(max_length=255)
    expires_in = models.PositiveIntegerField()
    scope = models.CharField(max_length=100)
    token_type = models.CharField(max_length=100)
    expires_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.access_token
