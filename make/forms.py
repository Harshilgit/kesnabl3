from django import forms
from make.models import Make

class MakeForm(forms.ModelForm):

    class Meta:
        model = Make
        fields = ('master_name','make_name',)
        labels = {
        'master_name': 'Select Master Instrument',
        'make_name': 'Make',
        }
