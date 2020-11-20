from django.db import models

# Create your models here.

class Make(models.Model):
    master_name = models.ForeignKey('masterinstrument.MasterInstrumentType', on_delete=models.CASCADE, null=True)
    make_name = models.CharField(max_length=200)

    def __str__(self):
        return self.make_name
