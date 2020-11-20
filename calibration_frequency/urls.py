from django.urls import path
from . import views

urlpatterns = [


path('calibrationfrequency/', views.CalibrationFrequencyList.as_view(), name='calibrationfrequency_list' ),
path('calibrationfrequency/detail/<int:pk>', views.CalibrationFrequencyDetail.as_view(), name='calibrationfrequencydetail' ),
path('calibrationfrequency/create', views.CreateCalibrationFrequencyView.as_view(), name= 'createcalibrationfrequency' ),
path('calibrationfrequency/update/<int:pk>', views.UpdateCalibrationFrequencyView.as_view(), name= 'updatecalibrationfrequency'),
path('calibrationfrequency/delete/<int:pk>', views.DeleteCalibrationFrequencyView.as_view(), name='deletecalibrationfrequency'),

]
