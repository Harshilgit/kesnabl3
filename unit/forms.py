from django import forms
from unit.models import Unit

class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('location_name','unit_name',)
        labels = {
        'location_name': 'Select Location',
        'unit_name': 'Unit',
        }
