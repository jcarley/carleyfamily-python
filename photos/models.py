from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    mime_type = models.CharField(max_length=25)

    def __str__(self):
        return self.title
