from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class OrganizationListView(ListView):
    context_object_name = 'org_list'
    model = organization
    template_name = 'contact/organization_list.html'


class OrganizationDetailView(DetailView):
	context_object_name = 'org_detail'
	model = organization
	template_name = 'contact/organization_detail.html'


class CreateOrganizationView(CreateView):
	model = organization
	form_class = OrganizationForm
	template_name = 'contact/organization_form.html'
	success_url = reverse_lazy('list')



class UpdateOrganizationView(UpdateView):
	model = organization
	form_class = OrganizationForm
	template_name = 'contact/organization_form.html'
	success_url = reverse_lazy('list')



class DeleteOrganizationView(DeleteView):
	model = organization
	template_name = 'contact/organization_confirm_delete.html'
	success_url = reverse_lazy('list')



##################Contact######################


class ContactListView(ListView):
    context_object_name = 'con_list'
    model = contact
    template_name = 'contact/contact_list.html'


class ContactDetailView(DetailView):
	context_object_name = 'con_detail'
	model = contact
	template_name = 'contact/contact_detail.html'


class ContactCreateView(CreateView):
	model = contact
	form_class = ContactForm
	template_name = 'contact/contact_form.html'
	success_url = reverse_lazy('contact_list')



class ContactUpdateView(UpdateView):
	model = contact
	form_class = ContactForm
	template_name = 'contact/contact_form.html'
	success_url = reverse_lazy('contact_list')



class ContactDeleteView(DeleteView):
	model = contact
	template_name = 'contact/contact_confirm_delete.html'
	success_url = reverse_lazy('contact_list')




#############Category#################


class CategoryListView(ListView):
    context_object_name = 'cat_list'
    model = category
    template_name = 'contact/category_list.html'


class CategoryDetailView(DetailView):
	context_object_name = 'cat_detail'
	model = category
	template_name = 'contact/category_detail.html'


class CategoryCreateView(CreateView):
	model = category
	form_class = CategoryForm
	template_name = 'contact/category_form.html'
	success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
	model = category
	form_class = CategoryForm
	template_name = 'contact/category_form.html'
	success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
	model = category
	template_name = 'contact/category_confirm_delete.html'
	success_url = reverse_lazy('category_list')




############### ROLE #####################


class RoleListView(ListView):
    context_object_name = 'role_list'
    model = role
    template_name = 'contact/role_list.html'


class RoleDetailView(DetailView):
	context_object_name = 'role_detail'
	model = role
	template_name = 'contact/role_detail.html'


class RoleCreateView(CreateView):
	model = role
	form_class = RoleForm
	template_name = 'contact/role_form.html'
	success_url = reverse_lazy('role_list')


class RoleUpdateView(UpdateView):
	model = role
	form_class = RoleForm
	template_name = 'contact/role_form.html'
	success_url = reverse_lazy('role_list')


class RoleDeleteView(DeleteView):
	model = role
	template_name = 'contact/role_confirm_delete.html'
	success_url = reverse_lazy('role_list')





############### COUNTRY #####################


class CountryListView(ListView):
    context_object_name = 'ctry_list'
    model = country
    template_name = 'contact/country_list.html'


class CountryDetailView(DetailView):
	context_object_name = 'ctry_detail'
	model = country
	template_name = 'contact/country_detail.html'


class CountryCreateView(CreateView):
	model = country
	form_class = CountryForm
	template_name = 'contact/country_form.html'
	success_url = reverse_lazy('country_list')


class CountryUpdateView(UpdateView):
	model = country
	form_class = CountryForm
	template_name = 'contact/country_form.html'
	success_url = reverse_lazy('country_list')


class CountryDeleteView(DeleteView):
	model = country
	template_name = 'contact/country_confirm_delete.html'
	success_url = reverse_lazy('country_list')




############### STATE #####################


class StateListView(ListView):
    context_object_name = 'st_list'
    model = state
    template_name = 'contact/state_list.html'


class StateDetailView(DetailView):
	context_object_name = 'st_detail'
	model = state
	template_name = 'contact/state_detail.html'


class StateCreateView(CreateView):
	model = state
	form_class = StateForm
	template_name = 'contact/state_form.html'
	success_url = reverse_lazy('state_list')


class StateUpdateView(UpdateView):
	model = state
	form_class = StateForm
	template_name = 'contact/state_form.html'
	success_url = reverse_lazy('state_list')


class StateDeleteView(DeleteView):
	model = state
	template_name = 'contact/state_confirm_delete.html'
	success_url = reverse_lazy('state_list')




############### CITY #####################


class CityListView(ListView):
    context_object_name = 'ct_list'
    model = city
    template_name = 'contact/city_list.html'


class CityDetailView(DetailView):
	context_object_name = 'ct_detail'
	model = city
	template_name = 'contact/city_detail.html'


class CityCreateView(CreateView):
	model = city
	form_class = CityForm
	template_name = 'contact/city_form.html'
	success_url = reverse_lazy('city_list')


class CityUpdateView(UpdateView):
	model = city
	form_class = CityForm
	template_name = 'contact/city_form.html'
	success_url = reverse_lazy('city_list')


class CityDeleteView(DeleteView):
	model = city
	template_name = 'contact/city_confirm_delete.html'
	success_url = reverse_lazy('city_list')





############### INDUSTRY #####################


class IndustryListView(ListView):
    context_object_name = 'ind_list'
    model = industry
    template_name = 'contact/industry_list.html'


class IndustryDetailView(DetailView):
	context_object_name = 'ind_detail'
	model = industry
	template_name = 'contact/industry_detail.html'


class IndustryCreateView(CreateView):
	model = industry
	form_class = IndustryForm
	template_name = 'contact/industry_form.html'
	success_url = reverse_lazy('industry_list')


class IndustryUpdateView(UpdateView):
	model = industry
	form_class = IndustryForm
	template_name = 'contact/industry_form.html'
	success_url = reverse_lazy('industry_list')


class IndustryDeleteView(DeleteView):
	model = industry
	template_name = 'contact/industry_confirm_delete.html'
	success_url = reverse_lazy('industry_list')
