from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Condition
from .forms import ConditionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class ConditionList(ListView):
	model = Condition
	template_name = 'condition/condition_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class ConditionDetail(DetailView):
	context_object_name = 'cdn_detail'
	model = Condition
	template_name = 'condition/condition_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateConditionView(LoginRequiredMixin,CreateView):
	model = Condition
	form_class = ConditionForm
	success_url = reverse_lazy('condition_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateConditionView(LoginRequiredMixin,UpdateView):
	model = Condition
	form_class = ConditionForm
	success_url = reverse_lazy('condition_list')
	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class DeleteConditionView(LoginRequiredMixin,DeleteView):
	model = Condition
	success_url = reverse_lazy('condition_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
