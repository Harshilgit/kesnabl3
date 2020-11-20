from django.db import models

# Create your models here.

class MasterInstrumentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class MasterInstrument(models.Model):
    master_name = models.ForeignKey('MasterInstrumentType', on_delete=models.CASCADE)
    master_serialno = models.CharField(max_length=200,null=True)
    master_idno = models.CharField(max_length=200,null=True)
    range = models.CharField(max_length=200,null=True)
    inservice_date = models.DateField(null=True)
    inservice = models.BooleanField(default=False)
    make = models.ForeignKey('make.Make',on_delete=models.CASCADE)
    model = models.ForeignKey('model.Model',on_delete=models.CASCADE)
    least_count = models.FloatField(max_length=200,default="")
    resolution = models.FloatField(max_length=200,default="")
    initial_trac = models.CharField(max_length=200,default="")
    acceptance_criteria = models.CharField(max_length=200,default="")
    purchase_from = models.CharField(max_length=200,default="")
    purchase_order = models.CharField(max_length=200,default="")
    purchase_date = models.DateField(null=True)
    date_of_receipt = models.DateField(null=True)
    condition_of_receipt = models.CharField(max_length=200, null=True)
    date_of_inspection = models.DateField(null=True)
    software_details = models.CharField(max_length=200,default="")
    software_idno = models.CharField(max_length=200,default="")
    software_inservice = models.CharField(max_length=200,default="")
    manufacture_instruction = models.CharField(max_length=200,default="")
    national_international_standerd = models.CharField(max_length=200,default="")
    accuracy = models.FloatField(max_length=200,null=True)
    current_inst_condition = models.ForeignKey('condition.Condition',on_delete=models.CASCADE, null=True)
    amount = models.FloatField(max_length=200,null=True)
    parameter_calibrated = models.ForeignKey('parameter_calibrated.ParameterCalibrated',on_delete=models.CASCADE, null=True)
    referance_standard = models.CharField(max_length=200, null=True)
    ext_calibration_agency = models.CharField(max_length=200, null=True)
    cal_frequency = models.ForeignKey('calibration_frequency.CalibrationFrequency',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.master_name)

class MasterCertificate(models.Model):
    master_id = models.ForeignKey('MasterInstrumentType', on_delete=models.CASCADE, null=True)
    certificate_no = models.CharField(max_length=200)
    ulr_no = models.CharField(max_length=200,null=True)
    uncertainity = models.FloatField(blank=True,default=1)
    issue_date = models.DateField()
    exp_date = models.DateField()
    review_of_record = models.BooleanField(default=False)
    active_status = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True)

    def __Str__(self):
        return str(self.master_id)
