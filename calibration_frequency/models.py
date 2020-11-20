from django.db import models

# Create your models here.

class CalibrationFrequency(models.Model):
    frequency_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.frequency_name
