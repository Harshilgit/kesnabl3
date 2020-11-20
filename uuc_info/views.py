from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Target_Instrument
from .forms import Target_Instrument_Form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from masterinstrument.models import MasterInstrumentType, MasterInstrument


class UUCListView(ListView):
    context_object_name = 'target_list'
    model = Target_Instrument
    template_name = 'uuc_info/uuc_list.html'


class UUCDetailView(DetailView):
	context_object_name = 'target_detail'
	model = Target_Instrument
	template_name = 'uuc_info/uuc_detail.html'


class UUCCreateView(CreateView):
	model = Target_Instrument
	form_class = Target_Instrument_Form
	template_name = 'uuc_info/uuc_form.html'
	success_url = reverse_lazy('uuc_list')



class UUCUpdateView(UpdateView):
	model = Target_Instrument
	form_class = Target_Instrument_Form
	template_name = 'uuc_info/uuc_form.html'
	success_url = reverse_lazy('uuc_list')


class UUCDeleteView(DeleteView):
	model = Target_Instrument
	template_name = 'uuc_info/uuc_confirm_delete.html'
	success_url = reverse_lazy('uuc_list')
