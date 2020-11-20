from django import forms
from location.models import Location


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('location_id','location_name','temp','rh')
        labels = {
        'location_id': 'Location Id',
        'location_name': 'Location Name',
        'temp': 'Temperature',
        'rh': 'Percentage RH',
        }
