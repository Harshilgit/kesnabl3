from django.urls import path
from . import views

urlpatterns = [

    path('joblist/', views.JobListView.as_view(),name='job_list'),
    path('jobcreate/', views.CreateJobView.as_view(),name='createjob'),
    path('jobdetail/<int:pk>', views.JobDetailView.as_view(),name='detailjob'),
    path('jobupdate/<int:pk>', views.UpdateJobView.as_view(),name='updatejob'),
    path('jobdelete/<int:pk>', views.DeleteJobView.as_view(),name='deletejob'),

]
