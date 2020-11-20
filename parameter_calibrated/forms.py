from django import forms
from .models import ParameterCalibrated

class ParameterCalibratedForm(forms.ModelForm):

    class Meta:
        model = ParameterCalibrated
        fields = ('master_name','location_name','parameter_name')
        labels = {
        'master_name': 'Select Master Instrument',
        'location_name': 'Select LAB',
        'parameter_name': 'Parameter To Be Calibrated',
        }
