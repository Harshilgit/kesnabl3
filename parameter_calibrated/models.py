from django.db import models

# Create your models here.

class ParameterCalibrated(models.Model):
    master_name = models.ForeignKey('masterinstrument.MasterInstrumentType', on_delete=models.CASCADE, null=True)
    location_name = models.ForeignKey('location.Location', on_delete=models.CASCADE, null=True)
    parameter_name = models.CharField(max_length=200)

    def __str__(self):
        return self.parameter_name
