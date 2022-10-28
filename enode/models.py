from datetime import datetime
import logging
from django.db import models


class EnodeTokenModel(models.Model):

    access_token = models.CharField(max_length=255)
    expires_in = models.PositiveIntegerField()
    scope = models.CharField(max_length=100)
    token_type = models.CharField(max_length=100)
    expires_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.access_token

    def is_token_expired(self):
        now_timestamp = datetime.now().timestamp()
        expiration_timestamp = self.expires_date.timestamp()
        is_expired = now_timestamp > expiration_timestamp
        return is_expired
