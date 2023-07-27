from django.contrib import admin
from .models import Drug_Stor,drug_request,Register_Patient,Doctor,History_patient
# Register your models here.
admin.site.register(Drug_Stor)
admin.site.register(drug_request)
admin.site.register(Register_Patient)
admin.site.register(Doctor)
admin.site.register(History_patient)
