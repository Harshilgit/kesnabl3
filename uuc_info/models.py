from django.db import models
from masterinstrument.models import MasterInstrumentType, MasterInstrument


# Create your models here.

class Target_Instrument(models.Model):
    target_instrument_name = models.ForeignKey('masterinstrument.MasterInstrumentType',on_delete=models.CASCADE, null=True)
    workinstruction = models.CharField(max_length=200)
    Is_Standard = models.CharField(max_length=200)
    master_1 = models.ForeignKey('masterinstrument.MasterInstrument', related_name='%(class)s_master_name_1',on_delete=models.CASCADE)
    master_2 = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_master_name_2',on_delete=models.CASCADE)
    master_3 = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_master_name_3',on_delete=models.CASCADE, null=True)
    uncertainity = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str(self.target_instrument_name)
