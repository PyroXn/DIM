from django.contrib import admin

from .models import Patient, Address

admin.site.register(Patient)
admin.site.register(Address)
