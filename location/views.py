from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import Location
from .forms import LocationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



class LocationListView(ListView):
    
    model = Location
    template_name = 'location/location_list.html'


class LocationDetailView(DetailView):
	context_object_name = 'lcn_detail'
	model = Location
	template_name = 'location/location_detail.html'


class LocationCreateView(CreateView):
	model = Location
	form_class = LocationForm
	template_name = 'location/location_form.html'
	success_url = reverse_lazy('location_list')



class LocationUpdateView(UpdateView):
	model = Location
	form_class = LocationForm
	template_name = 'location/location_form.html'
	success_url = reverse_lazy('location_list')


class LocationDeleteView(DeleteView):
	model = Location
	template_name = 'location/location_confirm_delete.html'
	success_url = reverse_lazy('location_list')
