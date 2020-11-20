from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib import admin


urlpatterns = [
    path('', views.HomeView.as_view(),name='dashboard'),
    # path('login', views.LoginPageView.as_view(),name='login'),
    path('list', views.MasterInstrumentList.as_view(), name='masterinstrument_list' ),
    path('detail/<int:pk>', views.MasterInstrumentDetail.as_view(), name='masterinstrumentdetail' ),
    path('create', views.CreateMasterInstrumentView.as_view(), name= 'createmasterinstrument' ),
    path('update/<int:pk>', views.UpdateMasterInstrumentView.as_view(), name= 'updatemasterinstrument'),
    path('delete/<int:pk>', views.DeleteMasterInstrumentView.as_view(), name='deletemasterinstrument'),


    path('type/', views.MasterInstrumentTypeList.as_view(), name='masterinstrumenttype_list' ),
    path('type/detail/<int:pk>', views.MasterInstrumentTypeDetail.as_view(), name='masterinstrumenttypedetail' ),
    path('type/create', views.CreateMasterInstrumentTypeView.as_view(), name= 'createmasterinstrumenttype' ),
    path('type/update/<int:pk>', views.UpdateMasterInstrumentTypeView.as_view(), name= 'updatemasterinstrumenttype'),
    path('type/delete/<int:pk>', views.DeleteMasterInstrumentTypeView.as_view(), name='deletemasterinstrumenttype'),


    path('certificate', views.MasterInstrumentCertificateList.as_view(), name='masterinstrumentcertificate_list' ),
    path('certificate/detail/<int:pk>', views.MasterInstrumentCertificateDetail.as_view(), name='masterinstrumentcertificatedetail' ),
    path('certificate/create', views.CreateMasterInstrumentCertificateView.as_view(), name= 'createmasterinstrumentcertificate' ),
    path('certificate/update/<int:pk>', views.UpdateMasterInstrumentCertificateView.as_view(), name= 'updatemasterinstrumentcertificate'),
    path('certificate/delete/<int:pk>', views.DeleteMasterInstrumentCertificateView.as_view(), name='deletemasterinstrumentcertificate'),



    path('ajax/load-makes/', views.load_makes, name='ajax_load_makes'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),

    path('image_upload', image_view, name = 'image_upload'),
    path('success', success, name = 'success'),

    path('certificate/', views.CertificateListView.as_view(),name='certificate'),

    




]
