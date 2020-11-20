from django.urls import path
from . import views


urlpatterns = [

    path('testing_list', views.TestingList.as_view(), name='testing_list' ),
    path('testing_detail/<int:pk>', views.TestingDetail.as_view(), name='testing_detail' ),
    path('testing_create', views.CreateTestingView.as_view(), name= 'testing_create' ),
    path('testing_update/<int:pk>', views.UpdateTestingView.as_view(), name= 'testing_update'),
    path('testing_delete/<int:pk>', views.DeleteTestingView.as_view(), name='testing_delete'),

]
