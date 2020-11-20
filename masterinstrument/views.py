from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import MasterInstrument,MasterCertificate,MasterInstrumentType
from .forms import MasterInstrumentForm,MasterInstrumentTypeForm,MasterInstrumentCertificateForm,MasterInstrumentCertificateUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from model.models import Model
from make.models import Make
from contact.models import *
from condition.models import Condition
from parameter_calibrated.models import ParameterCalibrated
from calibration_frequency.models import CalibrationFrequency
from make.forms import MakeForm
from model.forms import ModelForm
from condition.forms import ConditionForm
from parameter_calibrated.forms import ParameterCalibratedForm
from calibration_frequency.forms import CalibrationFrequencyForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from testing_info.models import TestingInfo
from testing_info.forms import TestingInfoForm
from certificate.models import Certificate



class HomeView(TemplateView):
	template_name = 'masterinstrument/dashboard.html'

# class LoginPageView(TemplateView):
# 	template_name = 'masterinstrumen/login.html'


# masterinstrument

class MasterInstrumentList(ListView):
	model = MasterInstrument
	template_name = 'masterinstrument/masterinstrument_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class MasterInstrumentDetail(DetailView):
	context_object_name = 'mi_detail'
	model = MasterInstrument
	template_name = 'masterinstrument/masterinstrument_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateMasterInstrumentView(LoginRequiredMixin,CreateView):
	model = MasterInstrument
	form_class = MasterInstrumentForm
	success_url = reverse_lazy('masterinstrument_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateMasterInstrumentView(LoginRequiredMixin,UpdateView):
	model = MasterInstrument
	form_class = MasterInstrumentForm
	success_url = reverse_lazy('masterinstrument_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteMasterInstrumentView(LoginRequiredMixin,DeleteView):
	model = MasterInstrument
	success_url = reverse_lazy('masterinstrument_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


# MasterInstrumentType

class MasterInstrumentTypeList(ListView):
	model = MasterInstrumentType
	template_name = 'masterinstrument/masterinstrument_type_list.html'
	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class MasterInstrumentTypeDetail(DetailView):
	context_object_name = 'mit_detail'
	model = MasterInstrumentType
	template_name = 'masterinstrument/masterinstrument_type_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateMasterInstrumentTypeView(LoginRequiredMixin,CreateView):
	model = MasterInstrumentType
	form_class = MasterInstrumentTypeForm
	success_url = reverse_lazy('masterinstrumenttype_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class UpdateMasterInstrumentTypeView(LoginRequiredMixin,UpdateView):
	model = MasterInstrumentType
	form_class = MasterInstrumentTypeForm
	success_url = reverse_lazy('masterinstrumenttype_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteMasterInstrumentTypeView(LoginRequiredMixin,DeleteView):
	model = MasterInstrumentType
	success_url = reverse_lazy('masterinstrumenttype_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


# Master Instrument Certificate

class MasterInstrumentCertificateList(ListView):
	model = MasterCertificate
	template_name = 'masterinstrument/masterinstrumentcertificate_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class MasterInstrumentCertificateDetail(DetailView):
	context_object_name = 'mic_detail'
	model = MasterCertificate
	template_name = 'masterinstrument/masterinstrumentcertificate_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateMasterInstrumentCertificateView(CreateView):
	model = MasterCertificate
	form_class = MasterInstrumentCertificateForm
	success_url = reverse_lazy('masterinstrumentcertificate_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class UpdateMasterInstrumentCertificateView(UpdateView):
	model = MasterCertificate
	form_class = MasterInstrumentCertificateForm
	success_url = reverse_lazy('masterinstrumentcertificate_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteMasterInstrumentCertificateView(LoginRequiredMixin,DeleteView):
	model = MasterCertificate
	success_url = reverse_lazy('masterinstrumentcertificate_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


	####################################(Certificate)#########################################


class CertificateListView(ListView):
	context_object_name = 'certificate_list'
	model = TestingInfo
	queryset = TestingInfo.objects.all()
	template_name = 'masterinstrument/certificate.html'

	def get_context_data(self, **kwargs):
		context = super(CertificateListView, self).get_context_data(**kwargs)
		context['make'] = Make.objects.all()
		context['model'] = Model.objects.all()
		context['organization'] = organization.objects.all()
		context['certificate'] = Certificate.objects.all()
		context['condition'] = Condition.objects.all()
		

		return context





def load_models(request):
    make_id = request.GET.get('make')
    models = Model.objects.filter(make_id=make_id).order_by('model_name')
    return render(request, 'masterinstrument/model_dropdown_list_options.html', {'models': models})


def load_makes(request):
    master_name_id = request.GET.get('master_name')
    makes = Make.objects.filter(master_name_id=master_name_id).order_by('make_name')
    return render(request, 'masterinstrument/make_dropdown_list_options.html', {'makes': makes})



def success(request):
    return HttpResponse('successfully uploaded')

def image_view(request):

    if request.method == 'POST':
        form = MasterCertificateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MasterCertificateForm()
    return render(request, 'mastercertificate_form.html', {'form' : form})
