from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Register_Patient)
admin.site.register(models.Doctors)
admin.site.register(models.Nurses)
admin.site.register(models.Drug_Stor)
admin.site.register(models.Prescribe_Request)
admin.site.register(models.Patient_History)
admin.site.register(models.patient_nurse)