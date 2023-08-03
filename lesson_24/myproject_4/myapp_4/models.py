from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()