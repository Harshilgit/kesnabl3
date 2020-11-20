from django import forms
from .models import Target_Instrument
from masterinstrument.models import MasterInstrument, MasterInstrumentType


class Target_Instrument_Form(forms.ModelForm):

    class Meta:
        model = Target_Instrument
        fields = ('target_instrument_name','workinstruction','Is_Standard','master_1','master_2','master_3','uncertainity')
        labels = {
        'target_instrument_name': 'Instrument Name',
        'workinstruction': 'Work Instruction',
        'master_1': 'Master 1',
        'master_2': 'Master 2',
        'master_3': 'Master 3',
        'uncertainity': 'Uncertainity',
        }
