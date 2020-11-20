from django import forms
from . models import organization,contact,category,role,country, state, city, industry


class DateInput(forms.DateInput):
    input_type = 'date'


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = organization
        fields = ('name','website','email','address','phone_1','industry','notes','country','state','city')
        labels = {
        'name': 'Name',
        'website': 'Website',
        'email': 'Email Address',
        'address': 'Address',
        'phone_1': 'Contact 1',
        'industry': 'Industry',
        'notes': "Notes",
        'country': 'Country',
        'state': 'State',
        'city': 'City'
        }



class ContactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = ('name','mobile','email','dob','organization','category','role','category','role','anniversary','gender')
        labels = {
        'name': 'Name',
        'mobile': 'Contact No',
        'email': 'Email Address',
        'dob': 'Date Of Birth',
        'organization': 'Organization',
        'category': 'Category',
        'role': 'Department',
        'anniversary': 'Anniversary',
        'gender': 'Gender',
        }
        widgets = {
        'dob': DateInput(),
        'anniversary': DateInput()
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = category
        fields = ('name','description')
        labels = {
        'name': 'Name',
        'description': 'Description'
        }


class RoleForm(forms.ModelForm):

    class Meta:
        model = role
        fields = ('name','description','designation')
        labels = {
        'name': 'Department',
        'description': 'Description',
        'designation': 'Designation'
        }


class CountryForm(forms.ModelForm):

    class Meta:
        model = country
        fields = ('name',)
        labels = {
        'name': 'Name'
        }


class StateForm(forms.ModelForm):

    class Meta:
        model = state
        fields = ('country','name')
        labels = {
        'country': 'Select Country',
        'name': 'State Name'
        }


class CityForm(forms.ModelForm):

    class Meta:
        model = city
        fields = ('country','state','name')
        labels = {
        'country': 'Select Country',
        'state': 'Select State',
        'name': 'City Name'
        }


class IndustryForm(forms.ModelForm):

    class Meta:
        model = industry
        fields = ('name',)
        labels = {
        'name': 'Name'
        }
