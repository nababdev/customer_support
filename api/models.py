from django.db import models
from django.utils import timezone

class Message(models.Model):
    message = models.CharField(max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
