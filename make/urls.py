from django.urls import path
from . import views

urlpatterns = [


path('make/', views.MakeList.as_view(), name='make_list' ),
path('make/detail/<int:pk>', views.MakeDetail.as_view(), name='makedetail' ),
path('make/create', views.CreateMakeView.as_view(), name= 'createmake' ),
path('make/update/<int:pk>', views.UpdateMakeView.as_view(), name= 'updatemake'),
path('make/delete/<int:pk>', views.DeleteMakeView.as_view(), name='deletemake'),

]
