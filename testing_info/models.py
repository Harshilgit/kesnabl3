from django.db import models

# Create your models here.


class TestingInfo(models.Model):
    job_no = models.ForeignKey('job_info.JobInfo', on_delete=models.CASCADE)
    inst_job_id = models.CharField(max_length=200,null=True)
    inst_name = models.ForeignKey('uuc_info.Target_Instrument', on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    make = models.ForeignKey('make.Make',on_delete=models.CASCADE)
    model = models.ForeignKey('model.Model',on_delete=models.CASCADE)
    sr_no = models.CharField(max_length=200)
    id_no = models.CharField(max_length=200)
    least_count = models.FloatField(max_length=200,default="")
    accuracy = models.FloatField()
    low_range = models.FloatField()
    high_range = models.FloatField()
    unit = models.ForeignKey('unit.Unit',on_delete=models.CASCADE)
    inst_location = models.CharField(max_length=200)
    condition = models.ForeignKey('condition.Condition',on_delete=models.CASCADE)
    nabl = models.BooleanField()
    cal_frequency = models.ForeignKey('calibration_frequency.CalibrationFrequency',on_delete=models.CASCADE)
    sp_req = models.CharField(max_length=200)


    def __str__(self):
        return str(self.inst_job_id)


class CertDetails(models.Model):
    cert_no = models.ForeignKey('certificate.Certificate', on_delete=models.CASCADE)
    area_name = models.ForeignKey('testing_info.TestingInfo', on_delete=models.CASCADE)
    customer_name = models.ForeignKey('contact.organization', on_delete=models.CASCADE)
    equipment_id = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_id_no',on_delete=models.CASCADE)
    equipment_name = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_inst_name',on_delete=models.CASCADE)
    inst_id = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_sr_no',on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    make = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_make',on_delete=models.CASCADE)
    range = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_range',on_delete=models.CASCADE)
    cal_date = models.ForeignKey('certificate.Certificate',related_name='%(class)s_cal_date',on_delete=models.CASCADE)
    acceptance = models.ForeignKey('testing_info.TestingInfo',related_name='%(class)s_accuracy',on_delete=models.CASCADE)
    cal_due_date = models.ForeignKey('certificate.Certificate',related_name='%(class)s_cal_due_date',on_delete=models.CASCADE)
    master_name = models.ForeignKey('masterinstrument.MasterInstrument', on_delete=models.CASCADE)
    master_make = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_make',on_delete=models.CASCADE)
    master_sr_no = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_sr_no',on_delete=models.CASCADE)
    master_range = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_range',on_delete=models.CASCADE)
    master_accuracy = models.ForeignKey('masterinstrument.MasterInstrument',related_name='%(class)s_accuracy',on_delete=models.CASCADE)
    master_cert_no = models.ForeignKey('masterinstrument.MasterCertificate',related_name='%(class)s_cert_no',on_delete=models.CASCADE)
    master_valid = models.ForeignKey('masterinstrument.MasterCertificate',related_name='%(class)s_valid',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cert_no)
