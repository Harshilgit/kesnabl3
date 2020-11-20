from django.urls import path
from . import views

urlpatterns = [


path('unit/', views.UnitList.as_view(), name='unit_list' ),
path('unit/detail/<int:pk>', views.UnitDetail.as_view(), name='unitdetail' ),
path('unit/create', views.CreateUnitView.as_view(), name= 'createunit' ),
path('unit/update/<int:pk>', views.UpdateUnitView.as_view(), name= 'updateunit'),
path('unit/delete/<int:pk>', views.DeleteUnitView.as_view(), name='deleteunit'),

]
