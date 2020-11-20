from django.urls import path
from . import views

urlpatterns = [


path('parametercalibrated/', views.ParameterCalibratedList.as_view(), name='parametercalibrated_list' ),
path('parametercalibrated/detail/<int:pk>', views.ParameterCalibratedDetail.as_view(), name='parametercalibrateddetail' ),
path('parametercalibrated/create', views.CreateParameterCalibratedView.as_view(), name= 'createparametercalibrated' ),
path('parametercalibrated/update/<int:pk>', views.UpdateParameterCalibratedView.as_view(), name= 'updateparametercalibrated'),
path('parametercalibrated/delete/<int:pk>', views.DeleteParameterCalibratedView.as_view(), name='deleteparametercalibrated'),

]
