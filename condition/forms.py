from django import forms
from .models import Condition

class ConditionForm(forms.ModelForm):

    class Meta:
        model = Condition
        fields = ('condition_name',)
        labels = {
        'condition_name': 'Condition Of Instrument',
        }
