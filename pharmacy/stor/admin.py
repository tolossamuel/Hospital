from django.contrib import admin
from .models import Drug_Stor,drug_request,LabTestName,LabTest,User_lab_temporary,LabResult
from .models import models
# Register your models here.
admin.site.register(Drug_Stor)
admin.site.register(drug_request)
class ListLab(admin.ModelAdmin):

    list_display = ('lab_tase_name', 'name')

admin.site.register(LabTestName)
admin.site.register(LabTest, ListLab)


admin.site.register(User_lab_temporary)
admin.site.register(LabResult)