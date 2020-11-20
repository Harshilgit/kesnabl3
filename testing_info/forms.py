from django import forms
from . models import TestingInfo
from model.models import Model
from make.models import Make
from condition.models import Condition
from parameter_calibrated.models import ParameterCalibrated
from calibration_frequency.models import CalibrationFrequency
from make.forms import MakeForm
from model.forms import ModelForm
from condition.forms import ConditionForm
from parameter_calibrated.forms import ParameterCalibratedForm
from calibration_frequency.forms import CalibrationFrequencyForm
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'



class TestingInfoForm(forms.ModelForm):

    class Meta:
        model = TestingInfo
        fields = ('job_no','inst_job_id','inst_name','location','make','model','sr_no','id_no','least_count','accuracy','low_range','high_range','unit','inst_location',
        'condition','nabl','cal_frequency','sp_req')
        labels = {
        'job_no': _('Select Job No'),
        'inst_job_id': _('Instrument Job ID'),
        'inst_name': _('Instrument Name'),
        'location': 'Location',
        'make': _('Make'),
        'model': _('Model'),
        'sr_no': 'Serial No',
        'id_no': 'ID No',
        'accuracy': 'Accuracy',
        'low_range': _('Low Range'),
        'high_range': _('High Range'),
        'least_count': _('Least Count'),
        'unit': 'Unit',
        'inst_location':'Instrument Location',
        'condition': 'Condition',
        'nabl': 'Nabl (Y/N)',
        'cal_frequency': 'Calibration Frequency',
        'sp_req': 'Special Request'
        }
