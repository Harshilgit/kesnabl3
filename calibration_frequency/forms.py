from django import forms
from .models import CalibrationFrequency

class CalibrationFrequencyForm(forms.ModelForm):

    class Meta:
        model = CalibrationFrequency
        fields = ('frequency_name',)
        labels = {
        'frequency_name': 'Calibration Frequency',
        }
