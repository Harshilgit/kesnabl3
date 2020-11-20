from django.urls import path
from . import views

urlpatterns = [

    path('orglist/', views.OrganizationListView.as_view(),name='list'),
    path('orgcreate/', views.CreateOrganizationView.as_view(),name='createorganization'),
    path('orgdetail/<int:pk>', views.OrganizationDetailView.as_view(),name='detailorganization'),
    path('orgupdate/<int:pk>', views.UpdateOrganizationView.as_view(),name='updateorganization'),
    path('orgdelete/<int:pk>', views.DeleteOrganizationView.as_view(),name='deleteorganization'),


    path('conlist/', views.ContactListView.as_view(),name='contact_list'),
    path('concreate', views.ContactCreateView.as_view(),name='contactcreate'),
    path('condetail/<int:pk>', views.ContactDetailView.as_view(),name='contactdetail'),
    path('conupdate/<int:pk>', views.ContactUpdateView.as_view(),name='contactupdate'),
    path('condelete/<int:pk>', views.ContactDeleteView.as_view(),name='contactdelete'),


    path('catlist/', views.CategoryListView.as_view(),name='category_list'),
    path('catcreate/', views.CategoryCreateView.as_view(),name='categorycreate'),
    path('catdetail/<int:pk>', views.CategoryDetailView.as_view(),name='categorydetail'),
    path('catupdate/<int:pk>', views.CategoryUpdateView.as_view(),name='categoryupdate'),
    path('catdelete/<int:pk>', views.CategoryDeleteView.as_view(),name='categorydelete'),


    path('rolelist/', views.RoleListView.as_view(),name='role_list'),
    path('rolecreate/', views.RoleCreateView.as_view(),name='rolecreate'),
    path('roledetail/<int:pk>', views.RoleDetailView.as_view(),name='roledetail'),
    path('roleupdate/<int:pk>', views.RoleUpdateView.as_view(),name='roleupdate'),
    path('roledelete/<int:pk>', views.RoleDeleteView.as_view(),name='roledelete'),


    path('countrylist/', views.CountryListView.as_view(),name='country_list'),
    path('countrycreate/', views.CountryCreateView.as_view(),name='countrycreate'),
    path('countrydetail/<int:pk>', views.CountryDetailView.as_view(),name='countrydetail'),
    path('countryupdate/<int:pk>', views.CountryUpdateView.as_view(),name='countryupdate'),
    path('countrydelete/<int:pk>', views.CountryDeleteView.as_view(),name='countrydelete'),



    path('statelist/', views.StateListView.as_view(),name='state_list'),
    path('statecreate/', views.StateCreateView.as_view(),name='statecreate'),
    path('statedetail/<int:pk>', views.StateDetailView.as_view(),name='statedetail'),
    path('stateupdate/<int:pk>', views.StateUpdateView.as_view(),name='stateupdate'),
    path('statedelete/<int:pk>', views.StateDeleteView.as_view(),name='statedelete'),


    path('citylist/', views.CityListView.as_view(),name='city_list'),
    path('citycreate/', views.CityCreateView.as_view(),name='citycreate'),
    path('citydetail/<int:pk>', views.CityDetailView.as_view(),name='citydetail'),
    path('cityupdate/<int:pk>', views.CityUpdateView.as_view(),name='cityupdate'),
    path('citydelete/<int:pk>', views.CityDeleteView.as_view(),name='citydelete'),



    path('industrylist/', views.IndustryListView.as_view(),name='industry_list'),
    path('industrycreate/', views.IndustryCreateView.as_view(),name='industrycreate'),
    path('industrydetail/<int:pk>', views.IndustryDetailView.as_view(),name='industrydetail'),
    path('industryupdate/<int:pk>', views.IndustryUpdateView.as_view(),name='industryupdate'),
    path('industrydelete/<int:pk>', views.IndustryDeleteView.as_view(),name='industrydelete'),

]
