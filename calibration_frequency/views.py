from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import CalibrationFrequency
from .forms import CalibrationFrequencyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class CalibrationFrequencyList(ListView):
	model = CalibrationFrequency
	template_name = 'calibration_frequency/calibration_frequency_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class CalibrationFrequencyDetail(DetailView):
	context_object_name = 'cfrn_detail'
	model = CalibrationFrequency
	template_name = 'calibration_frequency/calibration_frequency_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateCalibrationFrequencyView(LoginRequiredMixin,CreateView):
	model = CalibrationFrequency
	form_class = CalibrationFrequencyForm
	success_url = reverse_lazy('calibrationfrequency_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateCalibrationFrequencyView(LoginRequiredMixin,UpdateView):
	model = CalibrationFrequency
	form_class = CalibrationFrequencyForm
	success_url = reverse_lazy('calibrationfrequency_list')
	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class DeleteCalibrationFrequencyView(LoginRequiredMixin,DeleteView):
	model = CalibrationFrequency
	success_url = reverse_lazy('calibrationfrequency_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
