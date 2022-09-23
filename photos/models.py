from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    mime_type = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
