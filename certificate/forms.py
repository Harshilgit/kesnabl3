from django import forms
from certificate.models import Certificate

class DateInput(forms.DateInput):
    input_type = 'date'

class CertForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = ('inst_job_id','cert_number','cert_date','valid_date','issue_date','client')
        labels = {
        'inst_job_id': 'Job Id',
        'cert_number': 'Certificate Number',
        'cert_date': 'Certificate Date',
        'valid_date': 'Validity Date',
        'issue_date': 'Issue Date',
        'client': 'Client',
        }
        widgets = {
        'cert_date': DateInput(),
        'valid_date': DateInput(),
        'issue_date': DateInput()
        }
