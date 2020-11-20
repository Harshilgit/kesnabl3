from django.urls import path
from . import views


urlpatterns = [

    path('uuc_list', views.UUCListView.as_view(), name='uuc_list' ),
    path('uuc_detail/<int:pk>', views.UUCDetailView.as_view(), name='uuc_detail' ),
    path('uuc_create', views.UUCCreateView.as_view(), name= 'uuc_create' ),
    path('uuc_update/<int:pk>', views.UUCUpdateView.as_view(), name= 'uuc_update'),
    path('uuc_delete/<int:pk>', views.UUCDeleteView.as_view(), name='uuc_delete'),

]
