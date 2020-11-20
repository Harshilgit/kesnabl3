from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Model
from .forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class ModelList(ListView):
	model = Model
	template_name = 'model/model_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class ModelDetail(DetailView):
	context_object_name = 'mdl_detail'
	model = Model
	template_name = 'model/model_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateModelView(LoginRequiredMixin,CreateView):
	model = Model
	form_class = ModelForm
	success_url = reverse_lazy('model_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateModelView(LoginRequiredMixin,UpdateView):
	model = Model
	form_class = ModelForm
	success_url = reverse_lazy('model_list')
	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class DeleteModelView(LoginRequiredMixin,DeleteView):
	model = Model
	success_url = reverse_lazy('model_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
