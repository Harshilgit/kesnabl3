from django.urls import path
from . import views


urlpatterns = [

    path('cert_list', views.CertificateListView.as_view(), name='cert_list' ),
    path('cert_detail/<int:pk>', views.CertificateDetailView.as_view(), name='cert_detail' ),
    path('cert_create', views.CertificateCreateView.as_view(), name= 'cert_create' ),
    path('cert_update/<int:pk>', views.CertificateUpdateView.as_view(), name= 'cert_update'),
    path('cert_delete/<int:pk>', views.CertificateDeleteView.as_view(), name='cert_delete'),

]
