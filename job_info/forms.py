from django import forms
from . models import JobInfo
from location.models import Location
from contact.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):

    class Meta:
        model = JobInfo
        fields = ('job_no','dt_receipt','total_inst','location','party_name','gatepass')
        labels = {
        'job_no': 'Job NO',
        'dt_receipt': 'Date Of Receipt',
        'total_inst': 'Total No Of Instruments',
        'location': 'Calibration Location',
        'party_name': 'Name Of Organization',
        'gatepass': 'Gate Pass',
        }
        widgets = {
        'dt_receipt': DateInput()
        }
