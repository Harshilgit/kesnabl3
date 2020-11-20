from django.contrib import admin
from .models import organization,category,contact,role,country,state,city,industry

admin.site.register(organization)
admin.site.register(category)
admin.site.register(contact)
admin.site.register(role)
admin.site.register(country)
admin.site.register(state)
admin.site.register(city)
admin.site.register(industry)
