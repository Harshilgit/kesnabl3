from django.db import models

# Create your models here.

class Certificate(models.Model):
    inst_job_id = models.ForeignKey('testing_info.TestingInfo', on_delete=models.CASCADE)
    cert_number = models.CharField(max_length=200)
    cert_date = models.DateField()
    valid_date = models.DateField()
    issue_date = models.DateField()
    client = models.ForeignKey('contact.organization', on_delete=models.CASCADE)


    def __str__(self):
        return self.cert_number
