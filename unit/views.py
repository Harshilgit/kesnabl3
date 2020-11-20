from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Unit
from .forms import UnitForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class UnitList(ListView):
	model = Unit
	template_name = 'unit/unit_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class UnitDetail(DetailView):
	context_object_name = 'ut_detail'
	model = Unit
	template_name = 'unit/unit_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateUnitView(LoginRequiredMixin,CreateView):
	model = Unit
	form_class = UnitForm
	success_url = reverse_lazy('unit_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateUnitView(LoginRequiredMixin,UpdateView):
	model = Unit
	form_class = UnitForm
	success_url = reverse_lazy('unit_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteUnitView(LoginRequiredMixin,DeleteView):
	model = Unit
	success_url = reverse_lazy('unit_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
