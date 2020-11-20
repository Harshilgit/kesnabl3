from django.db import models

# Create your models here.

class Unit(models.Model):
    location_name = models.ForeignKey('location.Location', on_delete=models.CASCADE, null=True)
    unit_name = models.CharField(max_length=200)

    def __str__(self):
        return self.unit_name
