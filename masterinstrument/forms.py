from django import forms
from . models import MasterInstrument,MasterCertificate,MasterInstrumentType
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



class MasterInstrumentForm(forms.ModelForm):

    class Meta:
        model = MasterInstrument
        fields = ('master_name','master_serialno','master_idno','make','model','least_count','range','inservice_date','inservice',
        'resolution','initial_trac','acceptance_criteria','purchase_from','purchase_order','purchase_date','date_of_receipt','condition_of_receipt','date_of_inspection',
        'software_details','software_idno','software_inservice','manufacture_instruction','national_international_standerd','accuracy','current_inst_condition','amount','parameter_calibrated','referance_standard','ext_calibration_agency','cal_frequency')


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['make'].queryset = Make.objects.none()

            if 'master_name' in self.data:
                try:
                    master_name_id = int(self.data.get('master_name'))
                    self.fields['make'].queryset = Make.objects.filter(master_name_id=master_name_id).order_by('make_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['make'].queryset = self.instance.master_name.make_set.order_by('make_name')



## MAKE-MODEL DEPENDENT DROPDOWN ##
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['model'].queryset = Model.objects.none()

            if 'make' in self.data:
                try:
                    make_id = int(self.data.get('make'))
                    self.fields['model'].queryset = Model.objects.filter(make_id=make_id).order_by('model_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['model'].queryset = self.instance.make.model_set.order_by('model_name')




        labels = {
        'master_name': _('Select Master Instrument'),
        'master_serialno': _('Serial No'),
        'master_idno': _('Id No'),
        'make': _('Make'),
        'model': _('Model'),
        'range': _('Range'),
        'least_count': _('Least Count'),
        'inservice_date': _('Date of Place Inservice'),
        'inservice': _('Inservice'),
        'resolution': 'Resolution',
        'initial_trac': 'Initial Traceability',
        'acceptance_criteria': 'Acceptance Criteria',
        'purchase_from': 'Purchased From',
        'purchase_order': 'Purchased Order No',
        'purchase_date': 'Purchased Order Date',
        'date_of_receipt': 'Date Of Receipt',
        'condition_of_receipt': 'Condition Of Receipt',
        'date_of_inspection': 'Date Of Inspection',
        'software_details': 'Software Details',
        'software_idno': 'Software Id No',
        'software_inservice': 'Date Of Software Placed Inservice',
        'manufacture_instruction': "Manufacture's Instruction",
        'national_international_standerd': 'National/International Standards',
        'accuracy': 'Accuracy',
        'current_inst_condition': 'Current Instrument Condition',
        'amount': 'Amount',
        'parameter_calibrated': 'Parameter To Be Calibrated',
        'referance_standard': 'Referance IS Standard',
        'ext_calibration_agency': 'External Calibration Agency',
        'cal_frequency': 'Calibration Frequency'
        }
        widgets = {
        'inservice_date': DateInput(),
        'purchase_date': DateInput(),
        'date_of_receipt': DateInput(),
        'date_of_inspection': DateInput(),
        'software_inservice': DateInput()
        }







class MasterInstrumentTypeForm(forms.ModelForm):

    class Meta:
        model = MasterInstrumentType
        fields = ('name',)
        labels = {
        'name': _('Master Name')
        }




class MasterInstrumentCertificateForm(forms.ModelForm):

    class Meta:
        model = MasterCertificate
        fields = ('master_id','certificate_no','ulr_no','uncertainity','issue_date','exp_date','review_of_record','active_status','image')
        labels = {
        'master_id': _('Select Type'),
        'certificate_no': _('Certificate No'),
        'ulr_no': _('ULR No'),
        'uncertainity': _('Uncertainity'),
        'issue_date': _('Date Of Calibration'),
        'exp_date': _('Due Date'),
        'review_of_record': _('Review Of Record'),
        'active_status': _('Active Status'),
        'image': _('Upload Image')
        }

        widgets = {
        'issue_date': DateInput(),
        'exp_date': DateInput(),
        }





class MasterInstrumentCertificateUpdateForm(forms.ModelForm):

    class Meta:
        model = MasterCertificate
        fields = ('issue_date','exp_date','ulr_no','review_of_record','active_status')
        labels = {
        'issue_date': _('Issue date'),
        'exp_date': _('Expire Date'),
        'ulr_no': _('ULR No'),
        'review_of_record': _('Review Of Record'),
        'active_status': _('Active Status')
        }
        widgets = {
        'issue_date': DateInput(),
        'exp_date': DateInput()
        }


class MakeForm(forms.ModelForm):

    class Meta:
        model = Make
        fields = ('make_name',)
        labels = {
        'make_name': 'Make',
        }


class ModelForm(forms.ModelForm):

    class Meta:
        model = Model
        fields = ('make','model_name',)
        labels = {
        'make': 'Select Make',
        'model_name': 'Model',
        }
