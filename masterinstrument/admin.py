from django.contrib import admin
from masterinstrument.models import MasterInstrument,MasterCertificate,MasterInstrumentType
admin.site.register(MasterInstrument)
admin.site.register(MasterCertificate)
admin.site.register(MasterInstrumentType)
