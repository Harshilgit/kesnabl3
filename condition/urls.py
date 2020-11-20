from django.urls import path
from . import views

urlpatterns = [


path('condition/', views.ConditionList.as_view(), name='condition_list' ),
path('condition/detail/<int:pk>', views.ConditionDetail.as_view(), name='conditiondetail' ),
path('condition/create', views.CreateConditionView.as_view(), name= 'createcondition' ),
path('condition/update/<int:pk>', views.UpdateConditionView.as_view(), name= 'updatecondition'),
path('condition/delete/<int:pk>', views.DeleteConditionView.as_view(), name='deletecondition'),

]
