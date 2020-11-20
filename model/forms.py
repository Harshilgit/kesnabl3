from django import forms
from model.models import Model

class ModelForm(forms.ModelForm):

    class Meta:
        model = Model
        fields = ('make','model_name',)
        labels = {
        'make': 'Select Make',
        'model_name': 'Model',
        }
