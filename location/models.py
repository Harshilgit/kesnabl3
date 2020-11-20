from django.db import models

# Create your models here.

class Location(models.Model):
    location_id = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    temp = models.CharField(max_length=200, null=True)
    rh = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.location_name
