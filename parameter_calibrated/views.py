from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import ParameterCalibrated
from .forms import ParameterCalibratedForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class ParameterCalibratedList(ListView):
	model = ParameterCalibrated
	template_name = 'parameter_calibrated/parameter_calibrated_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class ParameterCalibratedDetail(DetailView):
	context_object_name = 'pc_detail'
	model = ParameterCalibrated
	template_name = 'parameter_calibrated/parameter_calibrated_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateParameterCalibratedView(LoginRequiredMixin,CreateView):
	model = ParameterCalibrated
	form_class = ParameterCalibratedForm
	success_url = reverse_lazy('parametercalibrated_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateParameterCalibratedView(LoginRequiredMixin,UpdateView):
	model = ParameterCalibrated
	form_class = ParameterCalibratedForm
	success_url = reverse_lazy('parametercalibrated_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteParameterCalibratedView(LoginRequiredMixin,DeleteView):
	model = ParameterCalibrated
	success_url = reverse_lazy('parametercalibrated_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
