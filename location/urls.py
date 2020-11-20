from django.urls import path
from . import views


urlpatterns = [

    path('location_list', views.LocationListView.as_view(), name='location_list' ),
    path('location_detail/<int:pk>', views.LocationDetailView.as_view(), name='location_detail' ),
    path('location_create', views.LocationCreateView.as_view(), name= 'location_create' ),
    path('location_update/<int:pk>', views.LocationUpdateView.as_view(), name= 'location_update'),
    path('location_delete/<int:pk>', views.LocationDeleteView.as_view(), name='location_delete'),

]
