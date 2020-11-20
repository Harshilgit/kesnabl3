from django.db import models
from location.models import Location


# Create your models here.

class JobInfo(models.Model):
    job_no = models.CharField(max_length=200)
    dt_receipt = models.DateField()
    total_inst = models.IntegerField()
    location = models.ForeignKey('location.Location',on_delete=models.CASCADE)
    party_name = models.ForeignKey('contact.organization',related_name='%(class)s_party_name',on_delete=models.CASCADE)
    gatepass = models.CharField(max_length=200)

    def __str__(self):
        return str(self.job_no)
