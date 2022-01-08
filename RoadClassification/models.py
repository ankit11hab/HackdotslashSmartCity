from django.db import models

# Create your models here.
class RoadComplains(models.Model):

    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    imageLocation = models.CharField(max_length=200)
    score = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.latitude + self.longitude}'