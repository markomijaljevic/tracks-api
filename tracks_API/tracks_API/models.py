from django.db import models


class Tracks(models.Model):
    title = models.CharField(max_length=1024)
    artist = models.CharField(max_length=1024)
    duration = models.FloatField()
    last_play = models.DateTimeField()
