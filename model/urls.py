from django.urls import path
from . import views

urlpatterns = [


path('model/', views.ModelList.as_view(), name='model_list' ),
path('model/detail/<int:pk>', views.ModelDetail.as_view(), name='modeldetail' ),
path('model/create', views.CreateModelView.as_view(), name= 'createmodel' ),
path('model/update/<int:pk>', views.UpdateModelView.as_view(), name= 'updatemodel'),
path('model/delete/<int:pk>', views.DeleteModelView.as_view(), name='deletemodel'),

]
