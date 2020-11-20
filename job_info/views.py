from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class JobListView(ListView):
    context_object_name = 'job_list'
    model = JobInfo
    template_name = 'job_info/job_list.html'


class JobDetailView(DetailView):
	context_object_name = 'job_detail'
	model = JobInfo
	template_name = 'job_info/job_detail.html'


class CreateJobView(CreateView):
	model = JobInfo
	form_class = JobForm
	template_name = 'job_info/job_form.html'
	success_url = reverse_lazy('job_list')



class UpdateJobView(UpdateView):
	model = JobInfo
	form_class = JobForm
	template_name = 'job_info/job_form.html'
	success_url = reverse_lazy('job_list')



class DeleteJobView(DeleteView):
	model = JobInfo
	template_name = 'job_info/job_confirm_delete.html'
	success_url = reverse_lazy('job_list')
