"""nabl_final1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from masterinstrument import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('masterinstrument.urls')),
    path('make/', include('make.urls')),
    path('model/', include('model.urls')),
    path('location/', include('location.urls')),
    path('unit/', include('unit.urls')),
    path('condition/', include('condition.urls')),
    path('calibration_frequency/', include('calibration_frequency.urls')),
    path('parameter_calibrated/', include('parameter_calibrated.urls')),
    path('contact/', include('contact.urls')),
    path('uuc_info/', include('uuc_info.urls')),
    path('job_info/', include('job_info.urls')),
    path('testing_info/', include('testing_info.urls')),
    path('certificate/', include('certificate.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
