from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import TestingInfo
from .forms import TestingInfoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *




class TestingList(ListView):
    context_object_name = 'testing_list'
    model = TestingInfo
    template_name = 'testing_info/testing_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class TestingDetail(DetailView):
	context_object_name = 'testing_detail'
	model = TestingInfo
	template_name = 'testing_info/testing_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateTestingView(LoginRequiredMixin,CreateView):
	model = TestingInfo
	form_class = TestingInfoForm
	success_url = reverse_lazy('testing_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateTestingView(LoginRequiredMixin,UpdateView):
	model = TestingInfo
	form_class = TestingInfoForm
	success_url = reverse_lazy('testing_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteTestingView(LoginRequiredMixin,DeleteView):
	model = TestingInfo
	success_url = reverse_lazy('testing_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
