from django.contrib import admin
from .models import TestingInfo,CertDetails
from import_export.admin import ImportExportModelAdmin

# admin.site.register(TestingInfo)
admin.site.register(CertDetails)
@admin.register(TestingInfo)
class ViewAdmin(ImportExportModelAdmin):
    pass
