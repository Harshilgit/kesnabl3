from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Make
from .forms import MakeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




class MakeList(ListView):
	model = Make
	template_name = 'make/make_list.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user


class MakeDetail(DetailView):
	context_object_name = 'mk_detail'
	model = Make
	template_name = 'make/make_detail.html'

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class CreateMakeView(LoginRequiredMixin,CreateView):
	model = Make
	form_class = MakeForm
	success_url = reverse_lazy('make_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class UpdateMakeView(LoginRequiredMixin,UpdateView):
	model = Make
	form_class = MakeForm
	success_url = reverse_lazy('make_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user

class DeleteMakeView(LoginRequiredMixin,DeleteView):
	model = Make
	success_url = reverse_lazy('make_list')

	# def username(request):
	# 	user = User.objects.get(username=request.user.username)
	# 	return user
