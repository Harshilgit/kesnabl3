from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Certificate
from .forms import CertForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



class CertificateListView(ListView):
    context_object_name = 'cert_list'
    model = Certificate
    template_name = 'certificate/cert_list.html'


class CertificateDetailView(DetailView):
	context_object_name = 'cert_detail'
	model = Certificate
	template_name = 'certificate/cert_detail.html'


class CertificateCreateView(CreateView):
	model = Certificate
	form_class = CertForm
	template_name = 'certificate/cert_form.html'
	success_url = reverse_lazy('cert_list')



class CertificateUpdateView(UpdateView):
	model = Certificate
	form_class = CertForm
	template_name = 'certificate/cert_form.html'
	success_url = reverse_lazy('cert_list')


class CertificateDeleteView(DeleteView):
	model = Certificate
	template_name = 'certificate/cert_confirm_delete.html'
	success_url = reverse_lazy('cert_list')
